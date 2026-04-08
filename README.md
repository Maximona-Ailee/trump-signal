# trump-signal# 🚀 TrumpPulse — MLOps Semester Project

## 👥 Group Members

* Chenghao Luo
* Suchanya Baiyam
* Rogerio Braunschweiger de Freitas Lima

---

## 📌 Project Overview

**TrumpPulse** is an MLOps-focused system designed to ingest, process, and analyze textual data from Trump Truth Social Dataset.

The primary goal is **not model performance**, but the design and implementation of a **robust, reproducible, and deployable MLOps pipeline**.

The system performs:

* 🧠 **Sentiment Classification** (positive / negative / neutral)
* ❓ **Question Answering (QA)** over Trump’s posts

This project aligns with Aalborg University’s MLOps requirements by emphasizing:

* End-to-end pipeline
* Deployment readiness
* Reproducibility
* Continuous or on-demand execution

---

## 🎯 Aim of the Project

The objective is to build a **production-ready MLOps pipeline** that includes:

* 📥 Data ingestion (initial + reusable)
* 🧹 Preprocessing
* 🧬 Feature representation (embeddings)
* 🤖 Model inference (sentiment + QA)
* 🌐 API-based deployment
* 🐳 Containerization (Docker)
* 🔁 Continuous or trigger-based execution

---

## 🏗️ System Architecture

```
        ┌────────────────────┐
        │ Hugging Face Dataset │
        └─────────┬──────────┘
                  ↓
        ┌────────────────────┐
        │ Data Ingestion     │
        └─────────┬──────────┘
                  ↓
        ┌────────────────────┐
        │ Preprocessing      │
        └─────────┬──────────┘
                  ↓
        ┌────────────────────┐
        │ Model Layer        │
        │ - Sentiment        │
        │ - QA (Embeddings)  │
        └─────────┬──────────┘
                  ↓
        ┌────────────────────┐
        │ FastAPI Service    │
        └─────────┬──────────┘
                  ↓
        ┌────────────────────┐
        │ Docker Container   │
        └────────────────────┘
```

---

## ⚙️ Pipeline Components

### 📥 Data Ingestion

* Data is loaded from Hugging Face
* Stored locally for reproducibility

### 🧹 Preprocessing

* Text cleaning
* Null filtering
* Basic normalization

### 🤖 Model Layer

#### Sentiment Analysis

* Pretrained transformer model
* Outputs:

  * Label (POSITIVE / NEGATIVE)
  * Confidence score

#### Question Answering (QA)

* Sentence embeddings using `SentenceTransformers`
* Semantic similarity search
* Returns most relevant Trump posts

---

## 🌐 API Deployment

The system is deployed using:
👉 FastAPI

### Available Endpoints

| Endpoint             | Description               |
| -------------------- | ------------------------- |
| `/`                  | Health check              |
| `/predict_sentiment` | Classify sentiment        |
| `/ask_question`      | Retrieve relevant answers |

---

## 🐳 Containerization

The entire system is containerized using Docker:

* Ensures reproducibility
* Enables easy deployment
* Supports continuous operation

---

## 🔁 Execution Strategy

The system supports:

* ✅ API-based interaction (on-demand)
* ✅ Continuous execution via server runtime
* 🔜 Future: scheduled jobs (cron / GitHub Actions)

---

## 📦 Artifact Management

The project stores:

* 📁 Raw data
* 📁 Processed data
* 📁 Model outputs (predictions)

This supports:

* Reproducibility
* Debugging
* Evaluation

---

## 📊 Evaluation & Monitoring (Basic)

* Logging of predictions
* API health monitoring
* Model output inspection

Future improvements may include:

* Model versioning
* Drift detection
* Performance tracking

---

## 🧪 How to Run the Project

### ▶️ Local Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Access:
👉 http://localhost:8000/docs

---

### 🐳 Docker Run

```bash
docker build -t trump-pulse .
docker run -p 8000:8000 trump-pulse
```

---

## 🚀 Future Work

* 📊 Market reaction modeling
* 📈 Time-series analysis
* 🧠 Advanced NLP models
* 🌍 Frontend dashboard (Streamlit)
* 🔄 Automated data pipelines

---

## ✅ Key Takeaways

* Focus on **MLOps, not model perfection**
* Demonstrates **end-to-end pipeline**
* Fully **containerized and deployable**
* Supports **real-time interaction via API**

---

## 📎 Repository

👉 (https://github.com/Rogersurf/trump-signal)

---

## 💡 Final Note

This project is designed to demonstrate a **working, scalable, and reproducible MLOps system**, aligned with academic requirements and real-world deployment practices.

---
