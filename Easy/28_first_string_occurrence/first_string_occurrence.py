def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

a = 'sabutsdd'
b = 'sad'

print(strStr(a, b))