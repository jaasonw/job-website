    
from datetime import datetime

import pandas as pd
import pytz
from pytz import timezone

from transform.util import (
    convert_relative_date_to_timestamp,
    get_years_of_experience,
    get_tech_stack,
)

def parse_linkedin(metadata):
    date_format = "%m/%d/%Y %I:%M:%S %p %Z"
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone("US/Pacific"))
    date = date.strftime(date_format)
    metadata["last_updated"] = [date]

    df = pd.read_csv("linkedin.csv")
    df["Date"] = df["Date"].apply(convert_relative_date_to_timestamp)
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

    metadata["high_experience"] = jobs_n - len(df)

    # remove rows that contain the TS or SCI
    num_ts_sci = len(df)
    df = df[~df["Description"].str.contains("TS/SCI")]
    metadata["ts_sci"] = num_ts_sci - len(df)

    # sort by date posted
    df = df.sort_values(by=["Date"], ascending=False)

    with open("blacklist.txt", "r") as f:
        blacklist = f.read().splitlines()

    # remove rows that contain blacklisted agencies
    num_blacklist = len(df)
    df = df[~df["Company"].str.contains("|".join(blacklist))]
    metadata["blacklist"] = num_blacklist - len(df)

    # convert 2023-07-18T17:11:43.566939 to 2023-07-18
    df["Date"] = df["Date"].str.split("T").str[0]

    # convert nan to blank string
    df = df.fillna("")

    return df

