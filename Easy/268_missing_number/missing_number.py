from test_cases import cases, evaluate_cases
from bisect import bisect_left

# store all possible values in a list and use binary search to find a value in the list, thinking about this
# it shouldn't be necessary as the number will have the index when created by the range function. So just
# pop the number, since it is the index as well.  Just remove the binary search.
def is_missing(nums: list[int]) -> int:
    missing = [x for x in range(len(nums)+1)]
    for num in nums:
        missing.pop(bisect_left(missing, num))
    return missing[0]


# solution without the binary search, and storing values in a dictionary for constant look up time instead
def is_missing_2(nums: list[int]) -> int:
    missing = {x: 'None' for x in range(len(nums)+1)}
    for num in nums:
        missing.pop(num)
    for key in missing:
        return key

nums = [0, 1, 2, 3, 4, 6, 7, 8]
is_missing_2(nums)
