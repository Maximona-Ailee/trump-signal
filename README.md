---
title: TrumpSignal
emoji: 📊
colorFrom: red
colorTo: blue
sdk: docker
pinned: false
---

# TrumpSignal 📊 updated version 2.0.0 (22/04/2025)

An MLOps pipeline that ingests Trump's Truth Social posts and generates market impact signals.

> **Disclaimer:** This project was developed solely for academic purposes as part of the Data Engineering and Machine Learning Operations in Business course at Aalborg University. It is not affiliated with, endorsed by, or intended to influence any political party, candidate, or movement. The analysis is purely technical and should not be interpreted as political commentary or financial advice.

---

## What it does

- Ingests Trump's Truth Social posts daily from HuggingFace
- Classifies posts by category (threatening, self-promotion, attacking, etc.)
- Predicts whether the next trading day will be high or low market impact
- Shows real-time stock price movements around each post
- Provides semantic search over all posts by topic

---

## Live Demo
Live Demo
🚀 https://huggingface.co/spaces/Ailee52/trump-signal
📦 Artifacts Repository: https://huggingface.co/datasets/Ailee52/trump-signal-artifacts

---

## Pipeline
chrissoria/trump-truth-social (HuggingFace Dataset)
        ↓ updated daily by source
GitHub Actions (5:00 AM UTC daily)
        ↓
1. init_db.py          → Pull fresh posts into SQLite
2. build_embeddings.py → Rebuild MiniLM-L6-v2 vectors
3. model_training.py   → Retrain XGBoost classifier
4. save_predictions.py → Log daily predictions
5. upload_artifacts.py → Push to Ailee52/trump-signal-artifacts
        ↓
HuggingFace Spaces (auto-restart)
        ↓
download_artifacts.py  → Download pre-built artifacts
        ↓
FastAPI (port 8000) + Streamlit (port 7860) via nginx```
```
---

## Tech Stack

| Layer | Technology |
|---|---|
| Data | HuggingFace Datasets, SQLite, DVC |
| ML | XGBoost, scikit-learn, sentence-transformers |
| Storage | SQLite, HuggingFace Hub (Ailee52/trump-signal-artifacts) |
| API | FastAPI, uvicorn |
| Frontend | Streamlit |
| Deployment | Docker, HuggingFace Spaces |
| Scheduling | APScheduler, GitHub Actions |
| Monitoring | FastAPI endpoints, GitHub Actions artifacts |
---

## Run Locally

**Requirements:** Docker

```bash
# Clone
git clone https://github.com/Rogersurf/trump-signal
cd trump-signal

# Build and run
docker build -t trump-signal .
docker run -p 8000:8000 -p 7860:7860 trump-signal
```

- Frontend: http://localhost:7860
- API docs: http://localhost:8000/docs

---

## Run without Docker

```bash
pip install -r requirements.txt
pip install -e .

# Terminal 1 — API
python -m uvicorn app.api.main:app --host 0.0.0.0 --port 8000

# Terminal 2 — Frontend
python -m streamlit run frontend/streamlitapp.py
```

---
```
## Project Structure
trump-signal/
├── app/
│   └── api/
│       ├── main.py          # FastAPI endpoints
│       └── monitoring.py    # Prometheus metrics
├── backend/
│   ├── model_training.py    # XGBoost training pipeline
│   ├── model_predict.py     # Inference
│   ├── save_predictions.py  # Daily prediction logging
│   ├── upload_artifacts.py  # Upload to HF Hub
│   └── download_artifacts.py # Download from HF Hub
├── backend_database/
│   ├── init_db.py           # Initialize SQLite from HF dataset
│   ├── daily_update.py      # Incremental updates
│   ├── build_embeddings.py  # Build semantic search index
│   ├── embeddings.py        # Search engine
│   └── data_api.py          # Data access layer
├── frontend/
│   ├── streamlitapp.py      # Main app entry point
│   ├── _pages/              # Page components
│   ├── _data/               # API client
│   └── _components/         # UI components
├── .github/
│   └── workflows/
│       └── data_update.yml  # Daily pipeline (5am UTC)
├── Dockerfile               # Container setup
├── nginx.conf               # Reverse proxy config
├── start.sh                 # Container startup script
└── requirements.txt
```
---

## Dataset

[chrissoria/trump-truth-social](https://huggingface.co/datasets/chrissoria/trump-truth-social) — updated daily, includes post categories, engagement metrics, stock price snapshots, and GDELT global event indicators.

---

## Team

- Rogerio Braunschweiger De Freitas Lima
- Chenhao Lou  
- Suchanya Baiyam (Ailee)

MSc Economics and Business Administration (Business Data Science)  
Aalborg University, 2026
