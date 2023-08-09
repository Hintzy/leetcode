from ds_templates import test_series as ts
from test_cases import cases

"""
The problem statement gives you a string 'stng' consisting of capital English letters and an integer K.  You are allowed
to replace 'k' letters within the string with another capital English letter. With this constraint in mind, the user 
must determine what is the longest substring that could be created of the same letter.  The length of this substring is
the value that is to be returned.

Method (O(n^2) time complexity, semi brute force solution):

initialize max_ss_len = 1
for each char in the string (enumerated: i, char):
    1) if the length of the substring from the current slice position to the end of the stringr is less than or equal
     to the current max_ss_len, then return the current max_ss_len
     
    2) initialize ss_len as 1 and diff_count as k for each char loop.  Iterate through the chars ahead of the current
    positions and decrement diff_count by 1 each time a char differs from the current char (while diff_count, with a 
    diff_count -= 1 each time a different char is encountered).
    
    3) when not diff count, do a max comparison between the current max_ss_len and the current ss_len, store in max len
    
 
"""


def longest_char_replacement(strg: str, k: int) -> int:
    max_ss_len = 1
    for i, char in enumerate(strg):

        # after the first max substring length has been determined, the algorithm will skip any repeat first characters
        # because they will always be shorter than the previously determined max substring length
        if i > 0 and strg[i] == strg[i-1]:
            continue

        # if the length of the substring from the current slice position to the end of the string is less than or equal
        # to the current max_ss_len, then return the current max_ss_len
        elif len(strg[i:]) <= max_ss_len:
            return max_ss_len

        ss_len, diff_count = 0, k
        ind = i
        while ind <= len(strg) - 1:
            ss_char = strg[ind]
            if ss_char != char and diff_count == 0:
                ss_len = len(strg[i:ind])
                max_ss_len = max(max_ss_len, ss_len)
                break
            elif ss_char != char:
                diff_count -= 1
            elif ss_char == char:
                ss_len = len(strg[i:ind+1])
            max_ss_len = max(max_ss_len, ss_len)
            ind += 1


    return max_ss_len

# print(longest_char_replacement('ABAB', 2))
# print(longest_char_replacement('ABABA', 1))



"""
Sliding window method:

Left/right pointers of the sliding window, both start at zero.
    - a hashmap for the letters and count that are currently in the string
    - variable (int) for max substring length


Iterate through all positions with the right pointer. (curr = s[r])

At each point, add right pointer character to the count hashmap.  

Check if the length of the current substring minus the max char count is less than or equal to the amt of max 
replacements. 
    If max is exceeded increment r and l to the right, remove one from the l pointer coutner character in the hashmap.
     
    If not max, continue to the next iteration and move r to the right.
    Calc the length of the max substring length.  (max_sl = max(max_sl, r-l+1))
   


"""
def longest_char_replacement_sliding_window(s: str, k: int) -> int:
    chr_count, max_sl, l = {}, 0, 0
    for r in range(len(s)):
        curr, s_len = s[r], r - l + 1
        chr_count[curr] = chr_count.get(curr, 0) + 1
        if s_len - max(chr_count.values()) <= k:
            max_sl = max(max_sl, r - l + 1)
            continue
        else:
            while s_len - max(chr_count.values()) > k: #condition:
                chr_count[s[l]] -= 1
                s_len -= 1
                l += 1

    return max_sl


ts.test_series(longest_char_replacement_sliding_window, cases)
