import os
import boto3


def upload_file_to_s3(local_file_path: str):
    bucket_name = os.getenv("AWS_S3_BUCKET_NAME")

    if not bucket_name:
        return {
            "uploaded": False,
            "reason": "AWS_S3_BUCKET_NAME not configured"
        }

    s3_client = boto3.client("s3")

    s3_key = local_file_path.replace("\\", "/")

    s3_client.upload_file(
        local_file_path,
        bucket_name,
        s3_key
    )

    return {
        "uploaded": True,
        "bucket": bucket_name,
        "s3_key": s3_key
    }