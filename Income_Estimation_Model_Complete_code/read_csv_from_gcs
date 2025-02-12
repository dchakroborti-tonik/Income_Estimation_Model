
def save_df_to_gcs(df, bucket_name, destination_blob_name, file_format='csv'):
    """Saves a pandas DataFrame to Google Cloud Storage.

    Args:
        df: The pandas DataFrame to save.
        bucket_name: The name of the GCS bucket.
        destination_blob_name: The name of the blob to be created.
        file_format: The file format to save the DataFrame in ('csv' or 'parquet').
    """

    # Create a temporary file
    if file_format == 'csv':
        temp_file = 'temp.csv'
        df.to_csv(temp_file, index=False)
    elif file_format == 'parquet':
        temp_file = 'temp.parquet'
        df.to_parquet(temp_file, index=False)
    else:
        raise ValueError("Invalid file format. Please choose 'csv' or 'parquet'.")

    # Upload the file to GCS
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(temp_file)

    # Remove the temporary file
    import os
    os.remove(temp_file)
    
