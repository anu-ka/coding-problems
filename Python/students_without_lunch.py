# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
import pytest


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students_round = 0
        for i in students:
            if i == 0:
                students_round += 1
        students_square = len(students) - students_round
        sandwich_round = 0
        for i in sandwiches:
            if i == 0:
                sandwich_round += 1
        sandwich_square = len(sandwiches) - sandwich_round
        i = 0
        while i < len(sandwiches):
            if sandwiches[i] == students[i]:
                if sandwiches[i] == 0:
                    students_round -= 1
                    sandwich_round -= 1
                else:
                    students_square -= 1
                    sandwich_square -= 1
                sandwiches = sandwiches[i + 1 :]
                students = students[i + 1 :]
                i = -1
            elif (sandwiches[i] == 0 and students_round == 0) or (
                sandwiches[i] == 1 and students_square == 0
            ):
                return students_round + students_square
            else:
                temp = students[i]
                students = students[i + 1 :]
                students.append(temp)
                i = -1
            i += 1
        return students_square + students_round


@pytest.mark.parametrize(
    ("students", "sandwiches", "result"),
    [
        ([1, 1, 0, 0], [0, 1, 0, 1], 0),
        ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3),
        ([1, 1, 1, 1], [0, 0, 0, 0], 4),
        ([1, 0], [0, 1], 0),
    ],
)
def test_countStudents(students: list[int], sandwiches: list[int], result: int) -> None:
    assert result == Solution().countStudents(students, sandwiches)
