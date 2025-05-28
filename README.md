# 📊 YouTube Analytics Data Engineering Project

This project demonstrates an end-to-end Data Engineering pipeline for collecting, transforming, and analyzing YouTube video data using Python, PySpark, and (simulated) GCP services.

---

## 🚀 Project Overview

The pipeline performs the following steps:

1. **Data Collection**

   - Fetches trending videos using the [YouTube Data API](https://youtube138.p.rapidapi.com)
   - Stores raw JSON responses locally in `data/raw/`

2. **Data Transformation**

   - Parses and cleans raw data using **PySpark**
   - Outputs a processed `.csv` file to `data/processed/`

3. **Cloud Simulation**
   - Uploads processed data to **Google Cloud Storage** (simulated)
   - Loads data from GCS into **BigQuery** for analysis (simulated)

---

## 🧱 Project Structure

```
youtube_analytics_project/yes
│
├── data/
│   ├── raw/                        # Raw JSON files from YouTube API
│   └── processed/                  # Transformed CSV files
│
├── scripts/
│   ├── fetch_youtube_data.py      # Fetch videos using YouTube API
│   ├── transform_youtube_data.py  # PySpark-based transformation
│   ├── upload_to_gcs.py           # GCS upload
│   └── load_into_bigquery.py      # BigQuery ingestion
│
├── gcp/
│   ├── schema/
│   │   └── bigquery_table_schema.json
│   └── config/
│       └── gcp_config.json
│
├── README.md                      # Main documentation
├── GCP_SIMULATION.md              # Detailed guide on GCP pipeline
└── requirements.txt               # Dependencies
```

---

## 🧪 Technologies Used

- **Python**
- **PySpark**
- **YouTube Data API**
- **Google Cloud Storage** _(simulated)_
- **BigQuery** _(simulated)_
- **Apache Airflow** _(simulated)_
- **Jupyter Notebook** _(optional)_

---

## 📄 GCP Simulation

While actual GCP access is not enabled, the entire cloud part is designed and structured as if it were ready for production. See [`GCP_SIMULATION.md`](./GCP_SIMULATION.md) for complete details.

---

## 👨‍💼 Author

- **Your Name**
- [LinkedIn](https://linkedin.com/in/your-profile) | [Portfolio](https://your-portfolio.com)
