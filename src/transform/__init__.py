import os
import sys

import pandas as pd
import pygsheets

from dotenv import load_dotenv
from pytz import timezone

from transform.parse_linkedin import parse_linkedin
from transform.parse_computerjobs import parse_computerjobs

load_dotenv()

def parse(upload=False):
    metadata = {}
    pd.set_option("display.max_rows", None)

    df_linkedin = parse_linkedin(metadata)
    df_compjobs = parse_computerjobs(metadata)
    df_merged = pd.concat([df_linkedin, df_compjobs])

    if upload or len(sys.argv) > 1 and sys.argv[1] == "--upload":
        gc = pygsheets.authorize(service_file="service_account_credential.json")

        sh = gc.open_by_key(os.getenv("GOOGLE_SHEETS_ID"))
        sh.sheet1.set_dataframe(df_merged, "A1", copy_head=True)

        print(metadata)
        metadata_df = pd.DataFrame.from_dict(metadata)
        print(metadata_df)
        sh.worksheet_by_title("Metadata").set_dataframe(
            metadata_df, "A1", copy_head=True
        )

        # requests.request("GET", os.environ.get("REVALIDATE_URL"))

