from ds_templates import test_series as ts
from test_cases import cases


"""
The problem statement gives you two strings: s1 and s2.
Prepare an algorithm that states if any permutation of s1 is a substring of s2


Solution Logic (sliding window approach):
- Store the chars/count from s1 in a hashmap (s1_hash)
- copy this hashmap (s1_temp = s1_hash.copy() )
- Set two pointers l,r = 0
    while r < len(s2) (so that the loop runs through the final element of the array):
        If current letter of s2 (curr = s2[r]) isn't in s1_temp:
            move the left and right pointers both past this letter, b/c the substring can't be a permutation before this
            point, (l = r + 1 and r = l) and reset the hashmap (s1_temp = s1_hash.copy() )
        
        While current letter (associated with 'r' pointer) of s2 is in s1_temp
            1) decrement that char from s1_temp
            2) if max s1_temp.values() == 0  (i.e. the decrement that just happened exhausted s1_hash), then return True
            2) if the addition of that char causes a letter count to go negative (i.e. that letter has exceeded the 
            count that exists in s1_hash), then move the 'l' pointer to the right until that letter count equals zero
            3) slide 'r' to the right. 
            
    If you exhausted all the letters by reaching the end of for loop on s2, then return False

"""

def permutationInString(s1: str, s2: str) -> bool:
    s1_hash = {}
    for char in s1:
        s1_hash[char] = s1_hash.get(char, 0) + 1
    l, r = 0, 0
    s1_temp = s1_hash.copy()
    while r < len(s2):
        if s2[r] not in s1_temp:
            l = r + 1
            r = l
            s1_temp = s1_hash.copy()
        elif s2[r] in s1_temp:
            cur = s2[r]
            s1_temp[cur] -= 1
            if max(s1_temp.values()) == 0:
                return True
            elif s1_temp[cur] < 0:
                while s1_temp[cur] < 0:
                    cur = s2[l]
                    s1_temp[cur] += 1
                    l += 1
            r += 1
    return False



# s1 = 'adc'
# s2 = 'dcda'
# print(permutationInString(s1, s2))

# ts.test_series(permutationInString, cases)
ts.test_case(permutationInString, cases, 8)
