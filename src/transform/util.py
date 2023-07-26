from datetime import datetime, timedelta
import re
import statistics


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
    years_of_experience = re.findall(r"\(?\d+[+-]?\d*\)? years?", description)

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
        "python",
        "javascript",
        "java",
        "c#",
        "php",
        "c++",
        "c",
        "r",
        "swift",
        "objective-c",
        "typescript",
        "ruby",
        "vb.net",
        "assembly",
        "go",
        "matlab",
        "vba",
        "kotlin",
        "scala",
        "rust",
        "dart",
        "perl",
        "elixir",
        "clojure",
        "groovy",
        "css",
        "sql",
    ]

    frameworks = [
        "react",
        "angular",
        "vue",
        "spring",
        "django",
        "flask",
        "laravel",
        "express",
        "ruby on rails",
        "asp.net",
        "bootstrap",
        "jquery",
        "symfony",
        "cakephp",
        "codeigniter",
    ]

    databases = [
        "mysql",
        "postgresql",
        "mariadb",
        "mongodb",
        "redis",
        "sqlite",
        "oracle",
        "elasticsearch",
        "cassandra",
        "mssql",
        "dynamodb",
        "firebase",
        "couchdb",
        "neo4j",
        "influxdb",
        "riak",
        "memcached",
        "hbase",
        "ravendb",
        "nosql",
    ]

    cloud_providers = [
        "aws",
        "azure",
        "google cloud",
    ]

    devops = [
        "docker",
        "kubernetes",
        "jenkins",
        "ansible",
        "terraform",
        "vagrant",
        "puppet",
        "chef",
        "bamboo",
        "gitlab",
        "circleci",
        "travis ci",
        "github actions",
        "bitbucket pipelines",
        "azure pipelines",
    ]

    misc = [
        "linux",
        "unix",
        "windows",
        "macos",
        "bash",
        "powershell",
        "git",
        "jira",
        "confluence",
        "kafka",
        "rest",
    ]

    tech_stack = set()

    for tech in [*languages, *frameworks, *databases, *cloud_providers, *devops, *misc]:
        if re.search(f"\\b{re.escape(tech)}\\b", description.lower()):
            tech_stack.add(tech)

    return [s.title() for s in list(tech_stack)]
