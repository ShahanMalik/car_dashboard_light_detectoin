import os
from dotenv import load_dotenv
from inference_sdk import InferenceHTTPClient
from warning_info import get_light_details, sort_by_severity

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("ROBOFLOW_API_KEY", "")

IMAGE_PATH = "original.jpg"
MODEL_ID   = "car-dashboard-sndt9/2"

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=API_KEY,
)

def run_detection(image_path: str) -> None:
    print(f"Running detection on: {image_path}")
    print("-" * 60)

    result = CLIENT.infer(image_path, model_id=MODEL_ID)

    predictions = result.get("predictions", [])
    if not predictions:
        print("No warning lights detected in the image.")
        return

    print(f"Detected {len(predictions)} warning light(s):\n")

    # Enrich each prediction with warning info
    enriched = []
    for pred in predictions:
        class_name = pred.get("class", "Unknown")
        confidence = pred.get("confidence", 0.0)
        info = get_light_details(class_name)
        enriched.append({
            "class":      class_name,
            "confidence": confidence,
            "severity":   info["severity"],
            "color":      info["color"],
            "meaning":    info["meaning"],
            "action":     info["action"],
            "category":   info["category"],
        })

    # Sort most critical first
    enriched = sort_by_severity(enriched)

    for i, item in enumerate(enriched, 1):
        print(f"{'='*60}")
        print(f"  {i}. {item['class']}")
        print(f"     Confidence : {item['confidence']*100:.1f}%")
        print(f"     Category   : {item['category']}")
        print(f"     Severity   : {item['severity']}  |  Color: {item['color']}")
        print(f"     Meaning    : {item['meaning']}")
        print(f"     Action     : {item['action']}")
    print("=" * 60)

if __name__ == "__main__":
    run_detection(IMAGE_PATH)
