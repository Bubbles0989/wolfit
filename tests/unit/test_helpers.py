from datetime import timedelta
from datetime import datetime
from datetime import date

from app import db
from app.helpers import less_than_day, pretty_date

# less than day 

def test_second_diff_less_60():
    new_int = 45
    new_string = less_than_day(new_int)
    assert new_string == str(new_int) + " seconds ago"

def test_second_diff_less_120():
    new_int = 110
    new_string = less_than_day(new_int)
    assert new_string == "a minute ago"

def test_second_diff_less_3600():
    new_int = 2350
    new_string = less_than_day(new_int)
    assert new_string == str(new_int // 60) + " minutes ago"

def test_second_diff_less_7200():
    new_int = 3687
    new_string = less_than_day(new_int)
    assert new_string == "an hour ago"

def test_second_diff_less_86400():
    new_int = 77777
    new_string = less_than_day(new_int)
    assert new_string == str(new_int // 3600) + " hours ago"

# pretty date

def test_time_is_int():
    now = datetime.utcnow()
    test_time = 1549836078
    test_diff = now - datetime.fromtimestamp(test_time)
    day_diff = test_diff.days

    return_string = pretty_date(test_time)
    assert return_string == str(day_diff // 365) + " years ago"

def test_time_is_false():
    test_time = False
    return_string = pretty_date(test_time)
    assert return_string == "just now"

def test_time_is_less_than_0_more_than_neg_1():
    pass

def test_time_is_yesterday():
    today = datetime.utcnow()
    yesterday = today - timedelta(days = 1)
    return_string = pretty_date(yesterday)
    assert return_string == "Yesterday"

def test_time_is_days_ago():
    pass

def test_time_is_weeks_ago():
    pass

def test_time_is_months_ago():
    pass

def test_time_is_years_ago():
    pass