# Changelog

\## \[2.0.0] - 2026-04-22



\### Added

\- HuggingFace Hub artifact storage (trump-signal-artifacts)

\- Daily GitHub Actions pipeline (5am UTC)

\- download\_artifacts.py — container downloads pre-built artifacts

\- upload\_artifacts.py — pipeline uploads fresh artifacts after retrain

\- save\_predictions.py — daily prediction logging

\- Evaluation artifacts saved per GitHub Actions run (90 day retention)

\- Auto-restart HF Spaces after pipeline completes



\### Fixed

\- load\_dotenv() added to main.py

\- Removed hardcoded database paths everywhere

\- Fixed wrong HF repo references (Rogersurf → Ailee52)

\- Removed upload from build\_embeddings.py

\- Fixed date picker to allow selection up to actual today

\- Fixed empty post message logic (actual\_today vs ds\_end)

\- Added sentence-transformers and python-dotenv to requirements.txt

\- Removed binary files from git history



\### Changed

\- Docker now downloads artifacts from HF Hub instead of building from scratch

\- start.sh now runs background\_update.py

\- GitHub Actions workflow runs daily instead of weekly







## v1.0.0 (2026-04-14)

### Frontend

* Daily feed with real Trump posts from dataset
* Live clock and NYSE market status
* Stock selector (12 stocks: S\&P500, QQQ, DJT, Gold, Bonds, Oil, Bitcoin, etc.)
* Sentiment filter removed — dataset classification used instead
* ML prediction — next day HIGH/LOW market impact (XGBoost model)
* Topic breakdown with custom date range picker
* Market impact page with period selector (This month/By month/By year/All time)
* Geopolitical page with GDELT data and period selector
* Q\&A semantic search with ChromaDB embeddings (all-MiniLM-L6-v2)
* All stock market impact in Q\&A results
* Export buttons on Market, Geopolitical, Topics pages
* No mock data — shows "data unavailable" when no data exists
* Dynamic max date from DB — auto-updates when dataset updates

### Data

* 32,429 Trump Truth Social posts (chrissoria/trump-truth-social)
* ChromaDB embeddings for semantic search
* SQLite database (truth\_social table)
* GDELT geopolitical signals

### ML

* XGBoost next-day market impact predictor
* Features: post categories, GDELT signals, rolling aggregates

