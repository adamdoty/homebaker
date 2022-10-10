"""Source: https://github.com/PyBites-Open-Source/pybites-tools/blob/main/pybites_tools/aws.py
Used to interface with aws s3 bucket for image storage."""

import argparse
import os
from typing import Optional
from django.conf import settings

import boto3


def upload_to_s3(file, acl="public-read"):
    s3_bucket = settings.AWS_STORAGE_BUCKET_NAME
    aws_key = settings.AWS_ACCESS_KEY_ID
    aws_secret = settings.AWS_SECRET_ACCESS_KEY
    aws_region = settings.AWS_S3_REGION_NAME

    session = boto3.Session(aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)

    s3 = session.resource("s3")
    response = s3.Bucket(s3_bucket).put_object(
        Key=file.name, Body=file.read(), ACL=acl
    )

    s3_file_link = f"https://{s3_bucket}.s3.{aws_region}.amazonaws.com/{response.key}"
    print(s3_file_link)

    return s3_file_link


def delete_from_s3(link: str, acl="public-read"):
    s3_bucket = settings.AWS_STORAGE_BUCKET_NAME
    aws_key = settings.AWS_ACCESS_KEY_ID
    aws_secret = settings.AWS_SECRET_ACCESS_KEY
    aws_region = settings.AWS_S3_REGION_NAME

    session = boto3.Session(aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)

    key = link.split('/')[-1]

    s3 = session.resource("s3")
    s3.Object(s3_bucket, key).delete()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument("-b", "--bucket")
    parser.add_argument("-a", "--acl")

    args = parser.parse_args()
    upload_to_s3(args.file, args.bucket, args.acl)


if __name__ == "__main__":
    main()
