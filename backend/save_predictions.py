"""Save daily predictions to a running log file."""
import json
import os
import pandas as pd
from datetime import date
from backend.model_predict import predict_latest

LOG_PATH = "artifacts/prediction_log.csv"

def save_predictions():
    os.makedirs("artifacts", exist_ok=True)
    
    # Get predictions for last 30 days
    result = predict_latest(days=30)
    result["run_date"] = str(date.today())
    result["date"] = result["date"].astype(str)
    
    # Append to existing log
    if os.path.exists(LOG_PATH):
        existing = pd.read_csv(LOG_PATH)
        combined = pd.concat([existing, result]).drop_duplicates(
            subset=["date", "run_date"]
        )
    else:
        combined = result
    
    combined.to_csv(LOG_PATH, index=False)
    print(f"Saved {len(result)} predictions to {LOG_PATH}")

if __name__ == "__main__":
    save_predictions()