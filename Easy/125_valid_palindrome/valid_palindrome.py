from time import time

class Solution:
    def isPalindrome_v1(self, s: str):
        s_strip = [char.lower() for char in s if char.isalnum()]
        s_rev = s_strip[::-1]
        return bool(s_strip == s_rev)

    def isPalindrome_v2(self, s: str):
        def isalnum(num):
            return bool(48 <= num < 58 or 65 <= num < 91 or 97 <= num < 123)
        s_strip = [char for char in s if isalnum(ord(char))]
        s_strip = ''.join(s_strip)
        s_strip = s_strip.lower()
        s_rev = s_strip[::-1]
        return bool(s_strip == s_rev)

    def isPalindrome_v3(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i, j = i + 1, j - 1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True

    def test_series(self, s):
        v1_start = time()
        print(v1_start)
        print(f'v1 - {self.isPalindrome_v1(s)}')
        v1_duration = time() - v1_start
        print(v1_duration)

        v2_start = time()
        print(v2_start)
        print(f'v2 - {self.isPalindrome_v2(s)}')
        v2_duration = time() - v2_start
        print(v2_duration)

        v3_start = time()
        print(v3_start)
        print(f'v3 - {self.isPalindrome_v3(s)}')
        v3_duration = time() - v3_start
        print(v3_duration)


if __name__ == '__main__':
    sol = Solution()

    # test cases
    str1 = '0P'  #true
    str2 = 'UPPERCAS!)(*#@$  E lETters' #
    str3 = 'nowawon'
    str4 = ''
    for _ in range(10000):
        str4 += '1'


    sol.test_series(str2)
