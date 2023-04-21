case1 = 'leetcode'
case2 = 'loveleetcode'
case3 = 'aabb'
case4 = 'aba'
case5 = 'stuff'
case6 = 'wiersdja'
cases = [case1, case2, case3, case4, case5, case6]

def firstUniqChar(s: str) -> int:
    chars = {}
    for i, char in enumerate(s):
        chars[char] = chars.get(char, 0) + 1
    index = -1
    for i in range(len(s)):
        if chars[s[i]] == 1:
            return i
    return index

for case in cases:
    print(firstUniqChar(case))