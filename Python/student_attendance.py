# https://leetcode.com/problems/student-attendance-record-i/
# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.


class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_list = []
        a = "A"
        l = "L"

        index = 0
        while index < len(s):
            if s[index] == a:
                absent_count += 1
            elif s[index] == l:
                late_list.append(index)
            index += 1
            if absent_count >= 2:
                return False
        # check if there are three consecutive numbers in late list
        i = 0
        if len(late_list) >= 3:
            while i < len(late_list) and i + 2 < len(late_list):
                if late_list[i + 2] - late_list[i] == 2:
                    return False
                i += 1

        return True


# print(Solution().checkRecord("PPALLP"))
# print(Solution().checkRecord("PAALLP"))
print(Solution().checkRecord("PPALLLP"))
# print(Solution().checkRecord("PPALLAPA"))
