import os
import sys

import pandas as pd
import pygsheets
from dotenv import load_dotenv
import requests

from transform.util import convert_relative_date_to_timestamp, get_years_of_experience

load_dotenv()


def main():
    df = pd.read_csv("linkedin.csv")
    df["Date"] = df["Date"].apply(convert_relative_date_to_timestamp)
    df["Years of Experience"] = df["Description"].map(get_years_of_experience)

    # print(df)

    # remove rows with more than 3 years of experience but keep Nans
    df = df[(df["Years of Experience"] <= 3) | (df["Years of Experience"].isnull())]

    # remove rows that contain the word senior
    df = df[~df["Title"].str.contains("Senior")]
    df = df[~df["Description"].str.contains("Senior")]

    # remove rows that contain the word mid
    df = df[~df["Title"].str.contains("Mid")]

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
    ]

    # remove rows that contain recruiting agencies
    for agency in recruiting_agencies:
        df = df[~df["Company"].str.contains(agency)]

    # convert 2023-07-18T17:11:43.566939 to 2023-07-18
    df["Date"] = df["Date"].str.split("T").str[0]

    # convert nan to blank string
    df = df.fillna("")

    print(df)

    if len(sys.argv) > 1 and sys.argv[1] == "--upload":
        gc = pygsheets.authorize(service_file="service_account_credential.json")

        sh = gc.open_by_key(os.getenv("GOOGLE_SHEETS_ID"))
        sh.sheet1.set_dataframe(df, "A1", copy_head=True)

        requests.request(os.environ.get("REVALIDATE_URL"))


if __name__ == "__main__":
    main()
