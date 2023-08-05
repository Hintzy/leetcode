from ds_templates import test_series as ts

"""
The problem statement states that we are given an array of unique integers in the range [1, n] inclusive, and the length
of the array is n+1, meaning that there must be a single integer which is duplicated.  The integer value of the duplicate
must be returned by the algorithm.

Further, the constraints are that the nums array must not be modified and the algorithm must use constant extra space.

A first solution that comes to mind to meet these constraints is to iterate through each number in the list, using list
slicing to check all the previous values in the list for a duplicate.  The worst case scenario would occur if the 
duplicate integers both occurred at the end of a very long list.  This would be O(n^2) time complexity, but would ensure
that the constant space constraint is satisfied.

If linear space were allow a hashmap of the seen values could be created and stored, which would easily reduce the time
to O(n) complexity.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 7]

def findDuplicateNum_n2(nums: list[int]) -> int:
    for i, num in enumerate(nums[1:]):
        if num in nums[:(i + 1)]:
            return num

# print(findDuplicateNum_n2(nums))


"""
Credit to Neetcode for pointing out it's a Floyd's tortoise and hare algorithm, but instead of using a linked list of
nodes with properties, it's simply an array with values that point to another position in the array.
"""

def findDuplicateNum_pointers(nums: list[int]) -> int:
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


print(findDuplicateNum_pointers(nums))
