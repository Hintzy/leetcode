str1 = '([])'
str2 = '()[]{}'
str3 = '(]'
str4 = '()(())[[][][]]{}'
str5 = '{[]}'
str6 = "){"

def isValid (s: str) -> bool:
    match = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    stack = []
    for char in s:
        if char in match.values():
            stack.append(char)
        else:
            if not stack or match[char] != stack[-1]:
                return False
            stack.pop()

    return True if not stack else False

print(isValid(str1))
print(isValid(str2))
print(isValid(str3))
print(isValid(str4))
print(isValid(str5))
print(isValid(str6))



