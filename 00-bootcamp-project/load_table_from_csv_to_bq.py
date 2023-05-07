from google.cloud import bigquery
from google.oauth2 import service_account
import os
import json

PROJECT_ID = 'myprojectde-384509'
DATASET = 'ded_bootcamp'
FILE_NAME =  ["events","addresses","order-items","orders","products","promos","users"]

keyfile = os.environ.get("KEYFILE_PATH")
service_account_info = json.load(open(keyfile))
credentials = service_account.Credentials.from_service_account_info(service_account_info)
project_id = "dataengineercafe"
client = bigquery.Client(
    project=PROJECT_ID,
    credentials=credentials,
)
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)
for x in FILE_NAME:
    with open (f"./data/{x}.csv", "rb") as source_file:
        job = client.load_table_from_file(source_file, f"{PROJECT_ID}.{DATASET}.{x}",job_config=job_config)
        table = client.get_table(f"{PROJECT_ID}.{DATASET}.{x}")
        print(
            "Loaded {} row and {} columns to {}".format(
                table.num_rows, len(table.schema), x
            )
        )