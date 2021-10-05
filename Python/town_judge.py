# https://leetcode.com/problems/find-the-town-judge/
import pytest


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        judge = -1
        people = {}
        prob_judge = {}
        for i in trust:
            people[i[0]] = 1
            try:
                prob_judge[i[1]] += 1
            except KeyError:
                prob_judge[i[1]] = 1
        for i in prob_judge:
            if i not in people and n - prob_judge[i] == 1:
                return i

        return judge


@pytest.mark.parametrize(
    ("n", "trust", "result"),
    [
        (2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (3, [[1, 3], [2, 3], [3, 1]], -1),
        (3, [[1, 2], [2, 3]], -1),
        (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3),
        (10, [], -1),
        (1, [], 1),
    ],
)
def test_findJudge(n: int, trust: list[list[int]], result: int) -> None:
    assert result == Solution().findJudge(n, trust)
