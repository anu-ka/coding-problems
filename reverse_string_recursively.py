import pytest


def reverse_string_recursively(data: str) -> str:
    if data == "" or data == None or len(data) == 1:
        return data
    return data[len(data) - 1] + reverse_string_recursively(data[0 : len(data) - 1])


@pytest.mark.parametrize(("data", "res"), [("anu", "una"), ("karthik", "kihtrak")])
def test_reverse_string_recursively(data: str, res: str) -> None:
    assert res == reverse_string_recursively(data)
