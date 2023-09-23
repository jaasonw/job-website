import os
import sys

import pytz
import pandas as pd
import pygsheets

from datetime import datetime
from pytz import timezone
from dotenv import load_dotenv

from transform.util import (
    convert_relative_date_to_timestamp,
    get_years_of_experience,
    get_tech_stack,
    convert_time_to_isoformat,
)

load_dotenv()

def parse(upload=False):
    metadata = {}
    pd.set_option("display.max_rows", None)

    df_linkedin = filter_data_to_df("linkedin", convert_relative_date_to_timestamp, metadata)
    df_compjobs = filter_data_to_df("computerjobs", convert_time_to_isoformat, metadata)
    df_merged = pd.concat([df_linkedin, df_compjobs])

    # print(df_merged)

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

def filter_data_to_df(company:str, dateConversion, metadata: dict):
    date_format = "%m/%d/%Y %I:%M:%S %p %Z"
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone("US/Pacific"))
    date = date.strftime(date_format)
    metadata["last_updated"] = [date]

    df = pd.read_csv(company + ".csv")
    df["Date"] = df["Date"].apply(dateConversion)
    df["Technologies"] = df["Description"].map(lambda x: ", ".join(get_tech_stack(x)))
    df["Years of Experience"] = df["Description"].map(get_years_of_experience)

    # remove rows with more than 3 years of experience but keep Nans
    jobs_n = len(df)
    df = df[(df["Years of Experience"] <= 3) | (df["Years of Experience"].isnull())]

    # remove rows that contain the word senior staff or principal
    df = df[~df["Title"].str.contains("Senior")]
    df = df[~df["Title"].str.contains("Sr.")]
    df = df[~df["Description"].str.contains("Senior")]
    df = df[~df["Description"].str.contains("Sr.")]
    df = df[~df["Title"].str.contains("Staff")]
    df = df[~df["Description"].str.contains("Staff")]
    df = df[~df["Title"].str.contains("Principal")]
    df = df[~df["Description"].str.contains("Principal")]

    # remove rows that contain the word mid
    df = df[~df["Title"].str.contains("Mid")]

    # remove rows that contain II or III
    df = df[~df["Title"].str.contains("II")]
    df = df[~df["Title"].str.contains("III")]

    if "high_experience" in metadata:
        metadata["high_experience"] += jobs_n - len(df)
    else:
        metadata["high_experience"] = jobs_n - len(df)

    # remove rows that contain the TS or SCI
    num_ts_sci = len(df)
    df = df[~df["Description"].str.contains("TS/SCI")]
    if "ts_sci" in metadata:
        metadata["ts_sci"] += num_ts_sci - len(df)
    else:
        metadata["ts_sci"] = num_ts_sci - len(df)

    # sort by date posted
    df = df.sort_values(by=["Date"], ascending=False)

    with open("blacklist.txt", "r") as f:
        blacklist = f.read().splitlines()

    # remove rows that contain blacklisted agencies
    num_blacklist = len(df)
    df = df[~df["Company"].str.contains("|".join(blacklist), na=False)]
    if "blacklist" in metadata:
        metadata["blacklist"] += num_blacklist - len(df)
    else:
        metadata["blacklist"] = num_blacklist - len(df)

    # convert 2023-07-18T17:11:43.566939 to 2023-07-18
    df["Date"] = df["Date"].str.split("T").str[0]

    # convert nan to blank string
    df = df.fillna("")

    return df


