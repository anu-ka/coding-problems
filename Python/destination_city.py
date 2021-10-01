# https://leetcode.com/problems/destination-city/
# You are given the array paths,
# where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
# Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore,
# there will be exactly one destination city.
import pytest


class Solution:
    def destCity1(self, paths: list[list[str]]) -> str:
        dict_paths = {i[0]: i[1] for i in paths}

        key = paths[0][0]
        while True:
            try:
                key = dict_paths[key]
            except KeyError:
                return key

    def destCity(self, paths: list[list[str]]) -> str:
        dict_paths = {}
        for i in paths:
            dict_paths[i[0]] = i[1]
        for i in dict_paths:
            if dict_paths[i] in dict_paths:
                pass
            else:
                return dict_paths[i]


@pytest.mark.parametrize(
    ("paths", "result"),
    [
        ([["B", "C"], ["D", "B"], ["C", "A"]], "A"),
        (
            [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
            "Sao Paulo",
        ),
    ],
)
def test_basic(paths: list[list[str]], result: str) -> None:
    assert result == Solution().destCity(paths)
