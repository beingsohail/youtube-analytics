# ☁️ GCP Simulation Guide

This document outlines how the GCP components would function if deployed, giving a complete picture of the end-to-end cloud data pipeline.

---

## 1️⃣ Upload to Google Cloud Storage

📍 Location: `gcp/upload_to_gcs.py`

### What It Does:

- Uses `google-cloud-storage` to upload the transformed `.csv` file to a GCS bucket.
- Simulates uploading to a bucket like `gs://youtube-pipeline-bucket/youtube_transformed.csv`

### Setup:

pip install google-cloud-storage

## 2️⃣ Load to BigQuery

📍 Location: gcp/load_to_bigquery.py

### Setup:

pip install google-cloud-bigquery

### Replace placeholders:

- project_id = "your-gcp-project-id"
- dataset_id = "youtube_dataset"
- table_id = "videos"
- gcs_uri = "gs://your-bucket-name/youtube_transformed.csv"

# Run:

python gcp/load_to_bigquery.py
