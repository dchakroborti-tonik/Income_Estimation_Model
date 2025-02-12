
def load_pickle_from_gcs(bucket_name, blob_path):
    """
    Load pickle file from Google Cloud Storage
    
    Parameters:
    bucket_name: Name of the GCS bucket
    blob_path: Path to the blob in the bucket
    
    Returns:
    Unpickled data
    """
    from google.cloud import storage
    import pickle
    import io
    
    # Initialize GCS client
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    
    # Download blob content into memory
    content = blob.download_as_bytes()
    
    # Load pickle data from memory
    pickle_data = pickle.loads(content)
    
    return pickle_data
