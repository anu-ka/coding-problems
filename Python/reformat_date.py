# https://leetcode.com/problems/reformat-date/

import pytest


class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }
        vals = date.split(" ")
        day = vals[0]
        mon = vals[1]
        year = vals[2]
        if day[1].isalpha():
            day = "0" + day[0:1]
        else:
            day = day[0:2]
        result = year + "-" + months[mon] + "-" + day
        return result


@pytest.mark.parametrize(
    ("date", "result"),
    [("20th Oct 2052", "2052-10-20"), ("6th Jun 1933", "1933-06-06")],
)
def test_reformatDate(date: str, result: str) -> None:
    assert result == Solution().reformatDate(date)
