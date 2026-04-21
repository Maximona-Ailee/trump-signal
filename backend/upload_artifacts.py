"""Upload artifacts to HuggingFace Hub after retraining."""
import os
from huggingface_hub import HfApi

HF_REPO = "Ailee52/trump-signal-artifacts"
TOKEN = os.environ.get("HF_TOKEN")
DATA_DIR = os.environ.get("TRUMPPULSE_DATA_DIR", "backend_database")

def upload():
    api = HfApi(token=TOKEN)
    
    files = [
        (f"{DATA_DIR}/trump_data.db", "trump_data.db"),
        (f"{DATA_DIR}/trump_embeddings.pkl", "trump_embeddings.pkl"),
        ("backend/model_artifacts/xgb_model.pkl", "xgb_model.pkl"),
        ("backend/model_artifacts/scaler.pkl", "scaler.pkl"),
        ("backend/model_artifacts/feature_cols.json", "feature_cols.json"),
        ("backend/model_artifacts/metrics.json", "metrics.json"),
    ]
    
    for local_path, repo_filename in files:
        if os.path.exists(local_path):
            print(f"Uploading {repo_filename}...")
            api.upload_file(
                path_or_fileobj=local_path,
                path_in_repo=repo_filename,
                repo_id=HF_REPO,
                repo_type="dataset"
            )
            print(f"Uploaded {repo_filename} ✅")
        else:
            print(f"Skipping {repo_filename} - file not found")
    
    print("All artifacts uploaded!")

if __name__ == "__main__":
    upload()