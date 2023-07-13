from ds_templates import test_series
from test_cases import cases

def binary_search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    mid = (l + r) // 2
    while l <= r:
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
        mid = (l + r) // 2
    return -1


test_series.test_series(binary_search, cases)
