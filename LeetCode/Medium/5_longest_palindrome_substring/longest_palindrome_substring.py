def longestPalindrome(s: str) -> str:
    def is_palindrome(s):
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return s

    if len(s) == 1:
        return s
    elif is_palindrome(s):
        return s
    else:
        # divide the string into two parts
        left = s[:-1]
        right = s[1:]

        # recursively find the longest palindromic substring in each part
        left_palindrome = longestPalindrome(left)
        right_palindrome = longestPalindrome(right)

        # return the longer of the two palindromic substrings
        if len(left_palindrome) > len(right_palindrome):
            return left_palindrome
        else:
            return right_palindrome


# print(longestPalindrome('abcdef'))

"""
"Moving window that is expanding method"
0th iteration - is full string palindrome
1nt - is len-1 shuffled through i = 0, 1 as starting indices
2th - is len-2 shuffled through i = 0, 1, 2 indicies
nth - is len-(n-1) shuffled through 

"""

def longestPalindrome(s: str) -> str:
    def is_palindrome(s):
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return s

    if len(s) == 1:
        return s

    for i in range(len(s)):
        ss_len = len(s) + 1 - i
        for j in range(i):
            if is_palindrome(s[j:ss_len + j]):
                return s[j:ss_len + j]
    else:
        return s[0]


print(longestPalindrome('aaaddaaaaf'))