"""
Fix My Ride — Warning Light Detection API
FastAPI app intended for Hugging Face Spaces (Docker SDK).
Exposes a single POST /detect endpoint that accepts an image and
returns enriched warning-light results as JSON.
"""

import os
import tempfile
import uvicorn
from typing import List

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from inference_sdk import InferenceHTTPClient
from warning_info import get_light_details, sort_by_severity

# ── Config ────────────────────────────────────────────────────
API_KEY  = os.getenv("ROBOFLOW_API_KEY", "")
MODEL_ID = "car-dashboard-sndt9/2"

if not API_KEY:
    raise RuntimeError(
        "ROBOFLOW_API_KEY environment variable is not set. "
        "Add it to your HF Space secrets or .env file."
    )

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=API_KEY,
)

# ── App ────────────────────────────────────────────────────────
app = FastAPI(
    title="Fix My Ride — Warning Light Detector",
    description="Upload a car dashboard image to detect and explain warning lights.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Response Models ────────────────────────────────────────────
class Detection(BaseModel):
    label:      str
    confidence: float       # 0.0 – 1.0
    category:   str
    severity:   str
    color:      str
    meaning:    str
    action:     str


class DetectionResponse(BaseModel):
    total:      int
    detections: List[Detection]


# ── Routes ─────────────────────────────────────────────────────
@app.get("/", summary="Health check")
def root():
    return {"status": "ok", "message": "Fix My Ride API is running."}


@app.post("/detect", response_model=DetectionResponse, summary="Detect warning lights")
async def detect(file: UploadFile = File(..., description="Dashboard image (jpg/png)")):
    """
    Upload a dashboard image and receive a list of detected warning lights
    sorted by severity (Critical → High → Medium → Low).
    """
    if file.content_type not in ("image/jpeg", "image/png", "image/jpg"):
        raise HTTPException(status_code=400, detail="Only JPEG and PNG images are accepted.")

    image_bytes = await file.read()

    # inference-sdk requires a file path, not a BytesIO object
    suffix = ".jpg" if "jpeg" in (file.content_type or "") else ".png"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(image_bytes)
        tmp_path = tmp.name

    try:
        result = CLIENT.infer(tmp_path, model_id=MODEL_ID)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Roboflow inference failed: {exc}")
    finally:
        os.remove(tmp_path)

    predictions = result.get("predictions", [])

    enriched = []
    for pred in predictions:
        class_name = pred.get("class", "Unknown")
        info = get_light_details(class_name)
        enriched.append({
            "label":      class_name,
            "confidence": round(pred.get("confidence", 0.0), 4),
            "category":   info["category"],
            "severity":   info["severity"],
            "color":      info["color"],
            "meaning":    info["meaning"],
            "action":     info["action"],
        })

    # Sort most critical first
    enriched = sort_by_severity(enriched)

    detections = [Detection(**item) for item in enriched]

    return DetectionResponse(total=len(detections), detections=detections)


# ── Entry point ────────────────────────────────────────────────
if __name__ == "__main__":
    # HF Spaces Docker expects port 7860
    uvicorn.run("app:app", host="0.0.0.0", port=7860, reload=False)
