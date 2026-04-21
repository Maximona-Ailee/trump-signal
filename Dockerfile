FROM python:3.12
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ curl nginx && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Environment variables — no hardcoding
ENV HF_HOME=/data/.huggingface
ENV TRUMPPULSE_DATA_DIR=/data/trump_pulse
ENV CHROMA_DB_PATH=/data/chroma_db

# Create directories
RUN mkdir -p $TRUMPPULSE_DATA_DIR $CHROMA_DB_PATH

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .
RUN pip install -e .

# Download artifacts from HF Hub
RUN python backend/download_artifacts.py

# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf
RUN chmod +x start.sh

EXPOSE 7860
CMD ["./start.sh"]