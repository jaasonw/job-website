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

load_dotenv()


def parse(upload=False):
    df = pd.read_csv("linkedin.csv")
    df["Date"] = df["Date"].apply(convert_relative_date_to_timestamp)
    df["Technologies"] = df["Description"].map(lambda x: ", ".join(get_tech_stack(x)))
    df["Years of Experience"] = df["Description"].map(get_years_of_experience)

    # print(df)

    # remove rows with more than 3 years of experience but keep Nans
    df = df[(df["Years of Experience"] <= 3) | (df["Years of Experience"].isnull())]

    # remove rows that contain the word senior
    df = df[~df["Title"].str.contains("Senior")]
    df = df[~df["Title"].str.contains("Sr.")]
    df = df[~df["Description"].str.contains("Senior")]
    df = df[~df["Description"].str.contains("Sr.")]

    # remove rows that contain the word mid
    df = df[~df["Title"].str.contains("Mid")]

    # remove rows that contain II or III
    df = df[~df["Title"].str.contains("II")]
    df = df[~df["Title"].str.contains("III")]

    # remove rows that contain the TS or SCI
    df = df[~df["Description"].str.contains("TS/SCI")]

    # sort by date posted
    df = df.sort_values(by=["Date"], ascending=False)

    recruiting_agencies = [
        "TEKsystems",
        "Robert Half",
        "CyberCoders",
        "Apex Systems",
        "Aerotek",
        "Collabera",
        "Kforce",
        "Kelly",
        "Jobot",
        "Insight Global",
        "Remotelyy.Us",
        "Revature",
        "SynergisticIT",
        "Cybertec",
        "Mindpal",
        "Cyberjin",
        "Get It Recruit",
        "Next Generation Technology",
        "Albin Engineering Services",
        "Ledgent Technology",
        "Trine IT Inc",
        "Magnus Technology Solutions",
        "Amick Brown",
        "FiSec Global Inc",
        "Global Hires, LLC",
        "Zortech Solutions",
        "Pattern Learning AI - Career & Tech Recruitment Reimagined!",
        "Patterned Learning AI",
        "Talentify.io",
        "Tata Consultancy Services",
        "BairesDev",
    ]

    # remove rows that contain recruiting agencies
    for agency in recruiting_agencies:
        df = df[~df["Company"].str.contains(agency)]

    # convert 2023-07-18T17:11:43.566939 to 2023-07-18
    df["Date"] = df["Date"].str.split("T").str[0]

    # convert nan to blank string
    df = df.fillna("")

    print(df)

    if upload or len(sys.argv) > 1 and sys.argv[1] == "--upload":
        gc = pygsheets.authorize(service_file="service_account_credential.json")

        sh = gc.open_by_key(os.getenv("GOOGLE_SHEETS_ID"))
        sh.sheet1.set_dataframe(df, "A1", copy_head=True)

        date_format = "%m/%d/%Y %I:%M:%S %p %Z"
        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone("US/Pacific"))
        date = date.strftime(date_format)

        # scuffed and i do not care
        last_updated = {"last_updated": [date]}
        last_updated = pd.DataFrame.from_dict(last_updated)
        print(last_updated)
        sh.worksheet_by_title("Metadata").set_dataframe(
            last_updated, "A1", copy_head=True
        )

        requests.request("GET", os.environ.get("REVALIDATE_URL"))
