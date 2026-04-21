#!/bin/bash
set -e

# Build embeddings if missing
if [ ! -f "$TRUMPPULSE_DATA_DIR/trump_embeddings.pkl" ]; then
    echo "[start.sh] Building embeddings..."
    python backend_database/build_embeddings.py
fi

echo "[start.sh] Starting API..."
uvicorn app.api.main:app --host 0.0.0.0 --port 8000 &

echo "[start.sh] Starting frontend..."
streamlit run frontend/streamlitapp.py --server.port 8501 --server.address 0.0.0.0 &

echo "[start.sh] Starting background updater..."
python backend_database/background_update.py &

echo "[start.sh] Waiting for Streamlit..."
until curl -s http://localhost:8501/_stcore/health > /dev/null 2>&1; do
    sleep 2
done

echo "[start.sh] Ready!"
exec nginx -g "daemon off;"