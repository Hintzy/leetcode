"""
The problem statement asks the user to develop an algorithm to find a number in a sorted array that may or may not have
been rotated 'k' times. The algorithm must have a time complexity of O(log(n)).

Test cases:
1) Empty array
2) Array w/ one number
3) Array has not been rotated
    - Num is first/last/middle array element
4) Array has been rotated once
    - Num is first/last/middle array element
5) Array has been rotated 'k' times
    - Num is first/last/middle array element

Logic:

The problem statement states that the solution must operate with time complexity of O(log(n)). This means that a binary
search must be used to find the number.

The solution method will use the following logic:
    - Define a binary search function
    - Define a 'find origin' function, which will find the index of the lowest number in a rotated array
    - Identify if the list has been rotated. (array[-1] < array[0]) (constant time) This must
        indicate if a rotation has taken place since the array consists of unique elements
        - If rotated, find the origin index
            - Compare search value to array[0]
                - If smaller, binary search the subset above the rotation origin
                - If larger, binary search the subset below the rotation origin
        - If not rotated, perform regular binary search on the full array.
"""


def search_array(nums: list[int], target: int) -> int:
    if not nums:
        return -1

    def binary_search(arr: list[int], tar: int, lo: int = 0, hi: int = None):
        if hi is None:
            hi = len(arr)-1
        mid = (lo + hi) // 2
        if arr[mid] == tar:
            return mid
        while lo < hi:
            if tar < arr[mid]:
                return binary_search(arr, tar, lo, mid-1)
            elif tar > arr[mid]:
                return binary_search(arr, tar, mid+1, hi)
        return -1

    def find_origin(arr: list[int], lo: int = 0, hi: int = None):
        if hi is None:
            hi = len(arr) - 1
        mid = (lo + hi) // 2
        if arr[lo] < arr[hi]:
            return lo
        elif arr[mid] < arr[mid - 1]:
            return mid
        elif arr[lo] > arr[mid]:
            return find_origin(arr, lo, mid-1)
        elif arr[mid] > arr[-1]:
            return find_origin(arr, mid+1, hi)

    if nums[0] > nums[-1]:
        origin = find_origin(nums)
        if nums[0] == target:
            return 0
        elif target > nums[0]:
            return binary_search(nums, target, lo=0, hi=origin)
        else:
            return binary_search(nums, target, lo=origin)
    else:
        return binary_search(nums, target)


# ____Alternate solution from Leetcode (trying to reproduce without looking)_______________________________________
"""
This solution method doesn't use recursion, and therefore should use less memory without sacrificing speed.  Still a 
two-pointer approach.
"""


def search_nonrecurse(nums: list[int], target: int) -> int:
    if not nums:
        return -1

    # set pointer locations and determine middle of array
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[-1]:
            if nums[mid] < target <= nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[0] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1

# ___Test Cases___________________________________________________________________________________________________

test_list_1 = [4, 5, 6, 7, 0, 1, 2]
# print(test_list)
#
# for _ in range(7):
#     test_list.append(test_list.pop(0))
#
# print(test_list)

print(search_nonrecurse(test_list_1, 0))
