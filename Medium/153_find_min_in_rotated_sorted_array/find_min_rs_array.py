from ds_templates import test_series
from test_cases import cases

"""
First check if the list is UNrotated (nums[0] < nums[-1] or len(nums) == 1).  Otherwise use a binary search to search
for the condition where nums[i] < nums[i-1]. This signifies the loop in the list, and the value nums[i] should be 
returned. You should never run into an index error with this algorithm b/c the only index where that would occur is on 
the first element. The binary search will never reach the first element because of the upfront test to see if it's an 
unrotated list. 

[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
"""

def find_min(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    if len(nums) == 1 or nums[0] < nums[-1]:
        return nums[0]
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < nums[mid-1]:
            return nums[mid]
        elif nums[mid] < nums[0]:
            r = mid - 1
        else:
            l = mid + 1
    return nums[l]


test_series.test_series(find_min, cases)
