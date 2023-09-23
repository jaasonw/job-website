from datetime import datetime, timedelta
from pytz import timezone

import re
import statistics

def convert_time_to_isoformat(date_string):
    date_format = "%m/%d/%Y %I:%M:%S %p"
    date = datetime.strptime(date_string, date_format)
    date = date.astimezone(timezone("US/Pacific"))
    return date.isoformat()

def convert_relative_date_to_timestamp(relative_date_string):
    relative_date_string = relative_date_string.lower()

    current_datetime = datetime.now()
    relative_date_delta = None

    if "week" in relative_date_string:
        weeks_ago = int(relative_date_string.split()[0])
        relative_date_delta = timedelta(weeks=weeks_ago)
    elif "month" in relative_date_string:
        months_ago = int(relative_date_string.split()[0])
        relative_date_delta = timedelta(days=months_ago * 30)
    elif "day" in relative_date_string:
        days_ago = int(relative_date_string.split(" ")[0])
        relative_date_delta = timedelta(days=days_ago)
    elif (
        "hour" in relative_date_string
        or "minute" in relative_date_string
        or "second" in relative_date_string
        or "now" in relative_date_string
    ):
        relative_date_delta = timedelta(seconds=1)

    if relative_date_delta:
        new_datetime = current_datetime - relative_date_delta
        timestamp = new_datetime.isoformat()
        return timestamp
    else:
        # Handle the case when the relative date string is not recognized
        print("Unable to recognize the relative date string.")
        return "N/A"


def get_years_of_experience(description):
    # get all things that look like "5 years", "5+ years", "1-4 years"
    years_of_experience = re.findall(
        r"\(?\d+[+-]?\d*\)? years?", description, re.IGNORECASE
    )

    try:
        # if there are no years of experience, return None
        if years_of_experience:
            # for each year of experience, get the average (for cases of ranges)
            years_of_experience = max(
                [
                    int(
                        statistics.mean(
                            [
                                int(e)
                                for e in re.split("[^0-9]", year.split(" ")[0])
                                # only include years of experience that are less than 12
                                # avoids edge cases like "in business for 100 years"
                                if e != "" and int(e) < 14
                            ]
                        )
                    )
                    for year in years_of_experience
                ]
            )
        else:
            years_of_experience = None
    except statistics.StatisticsError:
        years_of_experience = None
    return years_of_experience


def get_tech_stack(description):
    languages = [
        "Python",
        "Javascript",
        "Java",
        "C#",
        "PHP",
        "C++",
        "C",
        "R",
        "Swift",
        "Objective-C",
        "Typescript",
        "Ruby",
        "VB.net",
        "Assembly",
        "Go",
        "MATLAB",
        "VBA",
        "Kotlin",
        "Scala",
        "Rust",
        "Dart",
        "Perl",
        "Elixir",
        "Clojure",
        "Groovy",
        "CSS",
        "SQL",
    ]

    frameworks = [
        "React",
        "Angular",
        "Vue",
        "Spring",
        "Django",
        "Flask",
        "Laravel",
        "Express",
        "Ruby on Rails",
        "ASP.net",
        "Bootstrap",
        "jQuery",
        "Symfony",
        "Cakephp",
        "Codeigniter",
    ]

    databases = [
        "MySQL",
        "PostgreSQL",
        "MariaDB",
        "MongoDB",
        "Redis",
        "SQLite",
        "Oracle",
        "Elasticsearch",
        "Cassandra",
        "MsSQL",
        "DynamoDB",
        "Firebase",
        "CouchDB",
        "Neo4j",
        "InfluxDB",
        "Riak",
        "Memcached",
        "Hbase",
        "RavenDB",
        "NoSQL",
    ]

    cloud_providers = [
        "AWS",
        "Azure",
        "Google Cloud",
    ]

    devops = [
        "Docker",
        "Kubernetes",
        "Jenkins",
        "Ansible",
        "Terraform",
        "Vagrant",
        "Puppet",
        "Chef",
        "Bamboo",
        "Gitlab",
        "CircleCI",
        "Travis CI",
        "Github Actions",
        "Bitbucket Pipelines",
        "Azure Pipelines",
    ]

    misc = [
        "Linux",
        "Unix",
        "Windows",
        "MacOS",
        "Bash",
        "Powershell",
        "Git",
        "Jira",
        "Confluence",
        "Kafka",
        "REST",
    ]

    tech_stack = set()

    for tech in [*languages, *frameworks, *databases, *cloud_providers, *devops, *misc]:
        if re.search(f"\\b{re.escape(tech.lower())}\\b", description.lower()):
            tech_stack.add(tech)

    return list(tech_stack)
