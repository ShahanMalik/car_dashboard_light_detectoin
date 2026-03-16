# ── Hugging Face Spaces — Docker SDK ──────────────────────────
# Required labels for HF Spaces Docker deployment
# App runs on port 7860 (HF Spaces default)

FROM python:3.11-slim

# HF Spaces requires the app to run as a non-root user (uid 1000)
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Install system libraries required by opencv-python (used by inference-sdk)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
  && rm -rf /var/lib/apt/lists/*

# Install dependencies first (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY warning_info.py .

# Switch to non-root user
USER appuser

# Expose HF Spaces port
EXPOSE 7860

# ROBOFLOW_API_KEY must be set as a HF Space secret (not hardcoded here)
ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
