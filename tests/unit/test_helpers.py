import textwrap
from datetime import timedelta

from app import db
from app.helpers import less_than_day, pretty_date

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