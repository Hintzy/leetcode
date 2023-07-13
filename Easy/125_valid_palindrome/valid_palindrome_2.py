from ds_templates import test_series
from test_cases import tests

def valid_palindrome(s: str) -> bool:
    s = s.lower()
    s = [char for char in s if char.isalnum()]
    s = ''.join(s)

    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


test_series.test_series(valid_palindrome, tests)
