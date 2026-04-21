"""Download artifacts from HuggingFace Hub on container start."""
import os
from huggingface_hub import hf_hub_download

HF_REPO = "Ailee52/trump-signal-artifacts"
TOKEN = os.environ.get("HF_TOKEN")
DATA_DIR = os.environ.get("TRUMPPULSE_DATA_DIR", "/data/trump_pulse")
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_artifacts")

def download():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    files = [
        ("trump_data.db", DATA_DIR),
        ("trump_embeddings.pkl", DATA_DIR),
        ("xgb_model.pkl", MODEL_DIR),
        ("scaler.pkl", MODEL_DIR),
        ("feature_cols.json", MODEL_DIR),
        ("metrics.json", MODEL_DIR),
    ]
    
    for filename, local_dir in files:
        print(f"Downloading {filename}...")
        hf_hub_download(
            repo_id=HF_REPO,
            filename=filename,
            repo_type="dataset",
            local_dir=local_dir,
            token=TOKEN
        )
        print(f"Downloaded {filename} ✅")
    
    print("All artifacts ready!")

if __name__ == "__main__":
    download()