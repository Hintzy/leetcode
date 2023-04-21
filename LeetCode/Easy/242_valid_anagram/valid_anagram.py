from test_cases import cases, evaluate_cases

s = 'anagram'
t = 'anagra'
"""
Edge cases:
- One string is empty
- Both strings are empty
- One string is single char
- Both string are singel char
- Both string are identical (no rearrange)
- They are anagrams, but one has an additional of a single letter
- They are almost anagrams, but one is missing
- Generic test cases


"""


def is_anagram_1(s: str, t: str) -> bool:
    t_list = list(t)
    for let in s:
        if let in t_list:
            t_list.remove(let)
        else:
            return False
    if len(t_list) == 0:
        return True
    else:
        return False

def is_anagram_2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

evaluate_cases(is_anagram, cases)
