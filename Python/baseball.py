# https://leetcode.com/problems/baseball-game/
# You are keeping score for a baseball game with strange rules.
# The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.
# At the beginning of the game, you start with an empty record.
# You are given a list of strings ops,
# where ops[i] is the ith operation you must apply to the record and is one of the following:
# An integer x - Record a new score of x.
# "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
# "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
# Return the sum of all the scores on the record.

import pytest


class Solution:
    def calPoints(self, ops: list[str]) -> int:
        result = 0
        temp = []
        for i in ops:
            if i.lstrip("-").isdigit():
                val = int(i)
                temp.append(val)
            elif i == "D":
                prev = temp[len(temp) - 1]
                temp.append(prev * 2)
            elif i == "C":
                del temp[-1]
            elif i == "+":
                length = len(temp)
                num = temp[length - 1] + temp[length - 2]
                temp.append(num)
        for i in temp:
            result += i

        return result


@pytest.mark.parametrize(
    ("ops", "result"),
    [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1"], 1),
    ],
)
def test_basic(ops: list[int], result: int) -> None:
    assert result == Solution().calPoints(ops)
