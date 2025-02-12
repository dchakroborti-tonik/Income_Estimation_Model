
def read_csv_from_gcs(project_id, bucket_name, file_path):
  """Reads a CSV file from a GCS bucket into a pandas DataFrame.

  Args:
    project_id: The Google Cloud project ID.
    bucket_name: The name of the GCS bucket.
    file_path: The path to the CSV file within the bucket.

  Returns:
    A pandas DataFrame containing the CSV data.
  """

  storage_client = storage.Client(project=project_id)
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(file_path)

  with blob.open('r') as f:
    df = pd.read_csv(f)

  return df

