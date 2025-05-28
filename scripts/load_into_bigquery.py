# gcp/load_to_bigquery.py

from google.cloud import bigquery

def load_csv_from_gcs_to_bigquery():

    # loading a CSV file from GCS into a BigQuery table.

    project_id = "<gcp-project-id>"
    dataset_id = "youtube_dataset"
    table_id = "videos"
    gcs_uri = "gs://<bucket-name>/youtube_transformed.csv"

    client = bigquery.Client(project=project_id)

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    load_job = client.load_table_from_uri(
        gcs_uri,
        table_ref,
        job_config=job_config
    )

    print("Starting BigQuery job...")
    load_job.result()  # Waits for the job to complete.

    print(f"Loaded data into {table_ref}")

if __name__ == "__main__":
    load_csv_from_gcs_to_bigquery()
