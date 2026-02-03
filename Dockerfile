FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download model to avoid timeout on first use
RUN python -c "from transformers import VitsModel, AutoTokenizer; \
    VitsModel.from_pretrained('facebook/mms-tts-tgk'); \
    AutoTokenizer.from_pretrained('facebook/mms-tts-tgk')"

# Copy application files
COPY . .

# Create audio history directory
RUN mkdir -p audio_history

# Expose port
EXPOSE 8501

# Health check (optional - remove if curl not available)
# HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
#     CMD python -c "import requests; requests.get('http://localhost:8501/_stcore/health')" || exit 1

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]

