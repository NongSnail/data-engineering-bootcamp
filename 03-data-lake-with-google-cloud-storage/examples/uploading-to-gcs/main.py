import json
import os
import sys

from google.api_core import exceptions
from google.cloud import storage,bigquery
from google.oauth2 import service_account



def upload_blob(bucket_name,source_file_name,destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "narisara-100020"
    # # The path to your file to upload
    # source_file_name = "boxofficemojo_2023-04-24.csv"
    # # The ID of your GCS object
    # destination_blob_name = "2023-04-24/boxofficemojo"

    keyfile = "myprojectde-384509-8bca472ed8b6.json"
    service_account_info = json.load(open(keyfile))
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    project_id = "myprojectde-384509"

    storage_client = storage.Client(
        project=project_id,
        credentials=credentials,
    )
    bucket = storage_client.bucket(bucket_name)

    # try:
    #     bucket.delete_blob(blob_name=destination_blob_name)
    # except exceptions.NotFound as ex:
    #     print(f"File {destination_blob_name} not found")

    blob = bucket.blob(destination_blob_name)

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    # generation_match_precondition = 0
    # blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )


   


if __name__ == "__main__":
    bucket_name = "deb-bootcamp-100020"
    destination = "Greenery"
    datas =  ["events","addresses","order-items","orders","products","promos","users"]

    for x in datas:
        filename = f"./data/{x}.csv"
        blob_name = f"{destination}/{x}" 
        upload_blob(bucket_name,filename,blob_name)

    