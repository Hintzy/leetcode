str1 = '()'
str2 = '()[]{}'
str3 = '(]'
str4 = '()()()[][][){}'


def isValid (s: str) -> bool:
    correct = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    enum_str = [(i, let) for i, let in enumerate(s)]
    enum_str = [tupl for tupl in enum_str[::2]]
    for i, char in enum_str:
        if s[i+1] != correct[char]:
            return False
    return True


print(isValid(str1))
print(isValid(str2))
print(isValid(str3))
print(isValid(str4))

