from transform.util import convert_relative_date_to_timestamp
import datetime


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
