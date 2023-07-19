import pandas as pd
import pygsheets
import sys
from transform.util import convert_relative_date_to_timestamp, get_years_of_experience


def main():
    df = pd.read_csv("linkedin.csv")
    df["date"] = df["date"].apply(convert_relative_date_to_timestamp)
    df["years"] = df["description"].map(get_years_of_experience)

    # print(df)

    # remove rows with more than 3 years of experience but keep Nans
    df = df[(df["years"] <= 3) | (df["years"].isnull())]

    # remove rows that contain the word senior
    df = df[~df["title"].str.contains("Senior")]
    df = df[~df["description"].str.contains("Senior")]

    # remove rows that contain the word mid
    df = df[~df["title"].str.contains("Mid")]

    # remove rows that contain the TS or SCI
    df = df[~df["description"].str.contains("TS/SCI")]

    # sort by date posted
    df = df.sort_values(by=["date"], ascending=False)

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
    ]

    # remove rows that contain recruiting agencies
    df = df[~df["company"].isin(recruiting_agencies)]

    print(df)

    if len(sys.argv) > 1 and sys.argv[1] == "--upload":
        gc = pygsheets.authorize(service_file="service_account_credential.json")

        sh = gc.open_by_key("1Rp1yFWi6yJMhUGq2fkfGUhkmteScma5r9XkUEbqhq14")
        for index, row in df.iterrows():
            # convert nan to blank string
            row = row.fillna("")
            print(list(row))
            sh.sheet1.append_table(list(row), start="A1", end=None, dimension="ROWS")
