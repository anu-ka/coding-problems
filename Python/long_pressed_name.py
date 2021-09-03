# https://leetcode.com/problems/long-pressed-name/
# Your friend is typing his name into a keyboard. Sometimes, when typing a character c,
# the key might get long pressed, and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard.
# Return True if it is possible that it was your friends name,
# with some characters (possibly none) being long pressed.
import pytest


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        i = 0
        k = 0
        while i < len(name) and k < len(typed):
            if name[i] == typed[k]:
                i += 1
                k += 1
            elif i > 0 and name[i - 1] == typed[k]:
                k += 1
            elif name[i] != typed[k]:
                return False
        while k < len(typed):
            if name[i - 1] != typed[k]:
                return False
            k += 1
        if k == len(typed) and i < len(name):
            if name[i] != typed[k - 1]:
                return False
            k += 1
        return True


@pytest.mark.parametrize(
    ("name", "typed", "result"),
    [
        ("alex", "aalex", True),
        ("alex", "alex", True),
        ("saeed", "ssaaedd", False),
        ("rick", "kric", False),
        ("alex", "aaleexa", False),
        ("vtkgn", "vttkgnn", True),
        ("alexd", "ale", False),
        ("pyplrz", "ppyypllr", False),
    ],
)
def test_basic(name: str, typed: str, result: bool) -> None:
    assert result == Solution().isLongPressedName(name, typed)


# print(Solution().isLongPressedName("alex", "aalex"))  # True
# print(Solution().isLongPressedName("alex", "alex"))  # True
# print(Solution().isLongPressedName("saeed", "ssaaedd"))  # False
# print(Solution().isLongPressedName("rick", "kric"))  # False
# print(Solution().isLongPressedName("alex", "aaleexa"))  # False
# print(Solution().isLongPressedName("vtkgn", "vttkgnn"))  # True
# print(Solution().isLongPressedName("alexd", "ale"))  # False
# print(Solution().isLongPressedName("pyplrz", "ppyypllr"))  # False
