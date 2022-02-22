# https://leetcode.com/problems/build-an-array-with-stack-operations/
import pytest


class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result: list[int] = []
        push = "Push"
        pop = "Pop"
        i = target[0]
        k = target[len(target) - 1]
        present = 0
        while i <= k:
            result.append(push)
            if target[present] != i:
                result.append(pop)
            else:
                present += 1
            i += 1
        return result


print(Solution().buildArray([1, 3], 3))


@pytest.mark.parametrize(
    ("target", "n", "result"), [([1, 3], 3, ["Push", "Push", "Pop", "Push"])]
)
def test_buildArray(target: list[int], n: int, result: list[str]) -> None:
    assert result == Solution().buildArray(target, n)


# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
