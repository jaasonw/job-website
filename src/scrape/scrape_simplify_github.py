import pandas as pd
import requests

def get_simplify_github():
    response = requests.get(
        "https://raw.githubusercontent.com/SimplifyJobs/New-Grad-Positions/dev/.github/scripts/listings.json"
    )
    payload = response.json()

    for item in payload:
        item["locations"] = ", ".join(item["locations"])
        df = pd.DataFrame(payload)
        df = df[df["active"] is not False]
        df = df[df["is_visible"] is not False]
        df["date_updated"] = pd.to_datetime(df["date_updated"], unit="s")
        df["date_posted"] = pd.to_datetime(df["date_posted"], unit="s")
        df["date_updated"] = df["date_updated"].dt.date
        df["date_posted"] = df["date_posted"].dt.date
        df = df.sort_values(by="date_posted", ascending=False)
        df = df.drop(columns=["id", "is_visible", "sponsorship", "company_url"])
        df["description"] = ""
        df = df[
            [
                "url",
                "title",
                "company_name",
                "date_posted",
                "description",
                "locations",
                "source",
            ]
        ]
        df.rename(
            columns={
                "url": "URL",
                "title": "Title",
                "company_name": "Company",
                "date_posted": "Date",
                "description": "Description",
                "locations": "Location",
                "source": "Source",
            },
            inplace=True,
        )
        df.to_csv("simplify.csv", index=False)