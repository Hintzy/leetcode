"""
Solution:
2. store entire first word in a separate string variable (prefix)
1. iterate through list word by word starting with second word
3. for each subsequent word, test each letter at a time to see if it matches,
   store matches in temporary variable (cur_match).  When done with word,
   replace 'prefix' variable with cur_match.
4. return prefix when done with iteration
"""


strs1 = ['flower', 'flow', 'flight']
strs2 = ['dog', 'racecar', 'car']
strs3 = ['stuffness', 'stuffn', 'stuf']

def longest_common_prefix(strs):
    strs.sort(key=len)
    prefix = strs[0]
    for word in strs[1:]:
        word = word[:len(prefix)]
        cur_match = ''
        for i, letter in enumerate(word):
            if letter == prefix[i]:
                cur_match = cur_match + letter
        prefix = cur_match
        if len(prefix) == 0:
            return ''
    return prefix

print(longest_common_prefix(strs1))
print(longest_common_prefix(strs2))
print(longest_common_prefix(strs3))


