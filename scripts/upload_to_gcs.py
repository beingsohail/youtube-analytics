from google.cloud import storage
import os

# Path to the service account key
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/key.json"

def upload_to_gcs(bucket_name, source_file_path, destination_blob_name):
    """
    Uploads a file to Google Cloud Storage.

    :param bucket_name: GCS bucket name
    :param source_file_path: Local path to the file
    :param destination_blob_name: Name for the file in GCS
    """
    # Initialize a storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_path)

    print(f"File {source_file_path} uploaded to gs://{bucket_name}/{destination_blob_name}.")

# Example usage (commented out for demo)
# upload_to_gcs(
#     bucket_name="your-bucket-name",
#     source_file_path="data/processed/youtube_transformed.csv",
#     destination_blob_name="youtube/youtube_transformed.csv"
# )
