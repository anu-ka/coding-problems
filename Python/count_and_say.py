# https://leetcode.com/problems/count-and-say/
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
# which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of groups so that
# each group is a contiguous section all of the same character.
# Then for each group, say the number of characters, then say the character.
# To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
# Given a positive integer n, return the nth term of the count-and-say sequence.

import pytest


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        dict_nums = {1: "1"}
        i = 2
        while i <= n:
            res = self.cts(dict_nums[i - 1])
            dict_nums[i] = res
            i += 1
        return dict_nums[n]

    def cts(self, numbers: str) -> str:

        i = 0
        result = ""
        num = numbers[i]
        count = 1
        while i < len(numbers) - 1:
            if numbers[i + 1] != num:
                result += str(count) + num
                count = 1
                num = numbers[i + 1]
            else:
                count += 1
            i += 1
        result += str(count) + numbers[i]
        return result


@pytest.mark.parametrize(
    ("n", "result"),
    [
        (1, "1"),
        (2, "11"),
        (3, "21"),
        (4, "1211"),
        (5, "111221"),
        (10, "13211311123113112211"),
        (
            20,
            "11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211",
        ),
    ],
)
def test_basic(n: int, result: str) -> None:
    assert result == Solution().countAndSay(n)
