"""Download artifacts from HuggingFace Hub on container start."""
import os
import shutil
from huggingface_hub import hf_hub_download

HF_REPO = "Ailee52/trump-signal-artifacts"
TOKEN = os.environ.get("HF_TOKEN")
DATA_DIR = os.environ.get("TRUMPPULSE_DATA_DIR", "backend_database")
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_artifacts")

def download():
    print(f"DATA_DIR = {DATA_DIR}")
    print(f"MODEL_DIR = {MODEL_DIR}")
    print(f"Current working directory = {os.getcwd()}")
    
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

    for filename, target_dir in files:
        print(f"Downloading {filename} to {target_dir}...")
        cached = hf_hub_download(
            repo_id=HF_REPO,
            filename=filename,
            repo_type="dataset",
            token=TOKEN
        )
        target_path = os.path.join(target_dir, filename)
        shutil.copy2(cached, target_path)
        print(f"Copied {cached} → {target_path}")
        print(f"File exists: {os.path.exists(target_path)}")
        print(f"File size: {os.path.getsize(target_path)} bytes")

    print("All artifacts ready!")
    print(f"Contents of {DATA_DIR}: {os.listdir(DATA_DIR)}")

if __name__ == "__main__":
    download()