# https://leetcode.com/problems/day-of-the-year/
# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD,
# return the day number of the year.

import pytest


class Solution:
    def dayOfYear(self, date: str) -> int:
        months = {
            1: 31,
            2: 59,
            3: 90,
            4: 120,
            5: 151,
            6: 181,
            7: 212,
            8: 243,
            9: 273,
            10: 304,
            11: 334,
            12: 365,
        }
        temp_date = date.split("-")
        int_date = []
        for i in temp_date:
            int_date.append(int(i))

        (year, month, day) = int_date
        days = day

        if month > 1:
            days += months[month - 1]

        if month > 2 and year % 4 == 0:
            days += 1

        return days


@pytest.mark.parametrize(
    ("date", "result"), [("2003-03-01", 60), ("2012-01-02", 2), ("2016-02-09", 40)]
)
def test_dayOfYear(date: str, result: int) -> None:
    assert result == Solution().dayOfYear(date)
