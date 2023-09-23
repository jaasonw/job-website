from transform.util import (
    convert_relative_date_to_timestamp,
    convert_time_to_isoformat
)
import datetime

def test_convert_time_to_isoformat():
    time = "9/17/2023 11:46:49 AM"
    assert (
        convert_time_to_isoformat(time) == "2023-09-17T11:46:49-07:00"
    )

def test_convert_relative_date_to_timestamp():
    isotime = convert_relative_date_to_timestamp("1 day ago")
    assert (
        datetime.datetime.fromisoformat(isotime).day
        == (datetime.datetime.today() + datetime.timedelta(days=-1)).day
    )

    isotime = convert_relative_date_to_timestamp("7 days ago")
    assert (
        datetime.datetime.fromisoformat(isotime).day
        == (datetime.datetime.today() + datetime.timedelta(days=-7)).day
    )

    isotime = convert_relative_date_to_timestamp("1 week ago")
    assert (
        datetime.datetime.fromisoformat(isotime).day
        == (datetime.datetime.today() + datetime.timedelta(weeks=-1)).day
    )

    isotime = convert_relative_date_to_timestamp("7 weeks ago")
    assert (
        datetime.datetime.fromisoformat(isotime).day
        == (datetime.datetime.today() + datetime.timedelta(weeks=-7)).day
    )

    isotime = convert_relative_date_to_timestamp("1 month ago")
    assert (
        datetime.datetime.fromisoformat(isotime).day
        == (datetime.datetime.today() + datetime.timedelta(days=-30)).day
    )

    isotime = convert_relative_date_to_timestamp("7 months ago")
    assert (
        datetime.datetime.fromisoformat(isotime).day
        == (datetime.datetime.today() + datetime.timedelta(days=-30 * 7)).day
    )

    isotime = convert_relative_date_to_timestamp("Just now")
    assert (
        datetime.datetime.fromisoformat(isotime).day == (datetime.datetime.today()).day
    )

    isotime = convert_relative_date_to_timestamp("5 hours ago")
    assert (
        datetime.datetime.fromisoformat(isotime).day == (datetime.datetime.today()).day
    )

    isotime = convert_relative_date_to_timestamp("5 minutes ago")
    assert (
        datetime.datetime.fromisoformat(isotime).day == (datetime.datetime.today()).day
    )

    isotime = convert_relative_date_to_timestamp("5 minutes ago")
    assert (
        datetime.datetime.fromisoformat(isotime).day == (datetime.datetime.today()).day
    )
