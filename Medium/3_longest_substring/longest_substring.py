from ds_templates import test_series as ts
from test_cases import cases


"""
This first method works, but it's the brute force slow method.
It iterates through each index of the string as a starting position
    Within each iteration (0, 1, 2, 3), it uses the next index as the new starting position and builds from there
    looking at each letter progressively, if it's unique, or if it's a repeat. The unique/repeat comparison is performed
    by storing the values progressively in a hashmap. Once a repeat is identified, the loop for that current index is
    broken and moves onto the next index.

    Logic within each index loop:
    Create an empty hashmap called substring and an int variable max_len = 0:
        if next letter in string isn't in the hashmap,
            - add letter to hashmap
        if next letter is in the hashmap
            - empty the hashamp
            - compare sub_len against max_len
                if sub_len >:
                    replace max_len
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            substring = {}
            for let in s[i:]:
                if substring.get(let, 0) == 0:
                    substring[let] = 1
                else:
                    sub_len = len(substring)
                    if sub_len > max_len:
                        max_len = sub_len
                    substring = {let: 1}
                    sub_len = 1
                    break
            sub_len = len(substring)
            if sub_len > max_len:
                max_len = sub_len
        return max_len

# case_1 = 'abcddfghijk'
# sol = Solution()
# print(sol.lengthOfLongestSubstring(case_1))

# Leetcode solution that uses a sliding window

"""
def lengthOfLongestSubstring2(s: str) -> int:
    seen = {}
    max_sl = 0
    l = 0
    for r in range(len(s)):
        if s[r] not in seen:
            max_sl = max(max_sl, r-l+1)
        else:
            if s[r] < l:
                max_sl = max(max_sl, r-l+1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    return max_sl

print(lengthOfLongestSubstring2('abcdefg'))"""


# revisiting this problem after several months.  Using sliding window approach

"""
Left/right pointers of the sliding window, both start at zero.
    - a hashmap for the letters that are currently in the string
    - variable (int) for max substring length


Iterate through all positions with the right pointer. (curr = s[r)

At each point, check if right pointer character is in 'seen'.  

If is is in seen, while the character is in seen advance the left pointer, deleting each char it passes from the hashmap.
    While curr in seen:
        del s[l]
        l += 1
        
If it is not, set the length of the max substring length.  (max_sl = max(max_sl, r-l+1))
"""


def longestSubstring_sw(s: str) -> int:
    seen = {}
    max_sl = 0
    l, r = 0, 0
    for r in range(len(s)):
        curr = s[r]
        while curr in seen:
            del seen[s[l]]
            l += 1
        seen[curr] = True
        max_sl = max(max_sl, r-l+1)

    return max_sl


ts.test_series(longestSubstring_sw, cases)

