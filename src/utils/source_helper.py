import os
import boto3

def get_csv_local_path(filename: str) -> str:
    """
    Retorna o caminho local do CSV em ~/Desktop/Bases/<filename>.
    """
    base_dir = os.path.join(os.path.expanduser("~"), "Desktop", "Bases")
    return os.path.join(base_dir, filename)

def download_csv_if_s3(filename: str) -> str:
    """
    Se USE_S3=true, baixa do S3 para /tmp/dataflow/<filename>; 
    senão retorna ~/Desktop/Bases/<filename>.
    """
    use_s3 = os.getenv("USE_S3", "false").lower() in ("1", "true", "yes")
    if not use_s3:
        return get_csv_local_path(filename)

    bucket = os.getenv("S3_BUCKET_RAW")
    if not bucket:
        raise RuntimeError("Variável S3_BUCKET_RAW não definida, mas USE_S3=true.")

    s3_key = f"raw/{filename}"
    local_tmp_dir = os.path.join("/tmp", "dataflow")
    os.makedirs(local_tmp_dir, exist_ok=True)
    local_path = os.path.join(local_tmp_dir, filename)

    client = boto3.client(
        "s3",
        aws_access_key_id     = os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name           = os.getenv("AWS_REGION")
    )
    client.download_file(bucket, s3_key, local_path)
    return local_path
