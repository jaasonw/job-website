import os
import sys
from datetime import datetime

import pandas as pd
import pygsheets
import pytz
import requests
from dotenv import load_dotenv
from pytz import timezone

from transform.util import (
    convert_relative_date_to_timestamp,
    get_years_of_experience,
    get_tech_stack,
)


pd.set_option("display.max_rows", None)

load_dotenv()


def parse(upload=False):
    metadata = {}
    date_format = "%m/%d/%Y %I:%M:%S %p %Z"
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone("US/Pacific"))
    date = date.strftime(date_format)
    metadata["last_updated"] = [date]

    df = pd.read_csv("linkedin.csv")
    df["Date"] = df["Date"].apply(convert_relative_date_to_timestamp)
    df["Technologies"] = df["Description"].map(lambda x: ", ".join(get_tech_stack(x)))
    df["Years of Experience"] = df["Description"].map(get_years_of_experience)

    # print(df)

    # remove rows with more than 3 years of experience but keep Nans
    metadata["high_experience"] = len(df)
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

    metadata["high_experience"] = metadata["high_experience"] - len(df)

    # remove rows that contain the TS or SCI
    metadata["ts_sci"] = len(df)
    df = df[~df["Description"].str.contains("TS/SCI")]
    metadata["ts_sci"] = metadata["ts_sci"] - len(df)

    # sort by date posted
    df = df.sort_values(by=["Date"], ascending=False)

    with open("blacklist.txt", "r") as f:
        blacklist = f.read().splitlines()

    # remove rows that contain blacklisted agencies
    metadata["blacklist"] = len(df)
    print(~df["Company"].str.contains("|".join(blacklist)))
    df = df[~df["Company"].str.contains("|".join(blacklist))]
    metadata["blacklist"] = metadata["blacklist"] - len(df)

    # convert 2023-07-18T17:11:43.566939 to 2023-07-18
    df["Date"] = df["Date"].str.split("T").str[0]

    # convert nan to blank string
    df = df.fillna("")

    pd.set_option("display.max_rows", None)
    print(df)

    if upload or len(sys.argv) > 1 and sys.argv[1] == "--upload":
        gc = pygsheets.authorize(service_file="service_account_credential.json")

        sh = gc.open_by_key(os.getenv("GOOGLE_SHEETS_ID"))
        sh.sheet1.set_dataframe(df, "A1", copy_head=True)

        print(metadata)
        metadata_df = pd.DataFrame.from_dict(metadata)
        print(metadata_df)
        sh.worksheet_by_title("Metadata").set_dataframe(
            metadata_df, "A1", copy_head=True
        )

        # requests.request("GET", os.environ.get("REVALIDATE_URL"))
