
# Upload the model to GCS
def upload_model_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a model to a GCS bucket.

    Args:
        bucket_name: The name of the GCS bucket.
        source_file_name: The path to the local model file.
        destination_blob_name: The name of the blob to be created in GCS.
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name) 
    
