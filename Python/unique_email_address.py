# https://leetcode.com/problems/unique-email-addresses/
import pytest


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        dict_emails = {}
        for email in emails:
            i = 0
            proper_email = ""
            while i < len(email):
                if email[i] == ".":
                    proper_email += email[i + 1]
                    i += 1
                elif email[i].isalnum():
                    proper_email += email[i]
                elif email[i] == "+" or email[i] == "@":
                    break
                i += 1
            while email[i] != "@":
                i += 1
            if email[i] == "@":
                proper_email += email[i:]
            try:
                dict_emails[proper_email] += 1
            except KeyError:
                dict_emails[proper_email] = 1

        return len(dict_emails)


@pytest.mark.parametrize(
    ("emails", "result"),
    [
        (
            [
                "test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com",
            ],
            2,
        ),
        ([".anu@email.com", "anu@email.com"], 1),
        (
            [".anu@email.com", ".a+nu@email.com", ".anu+@email.com", ".anu+p@mail.com"],
            3,
        ),
        (
            [
                ".anu@email.com",
                ".a+nu@email.com",
                ".anu+@email.com",
                ".anu+p@email.com",
            ],
            2,
        ),
    ],
)
def test_numUniqueEmails(emails: list[str], result: int) -> None:
    assert result == Solution().numUniqueEmails(emails)
