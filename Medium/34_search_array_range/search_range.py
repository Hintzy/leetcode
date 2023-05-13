def search_range(nums: list[int], target: int) -> list[int, int]:

    def find_first(a_list, tar):
        index = -1
        left, right = 0, len(a_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if a_list[mid] == tar:
                index = mid
                right = mid - 1
            elif a_list[mid] > tar:
                right = mid - 1
            else:
                left = mid + 1
        return index

    def find_last(b_list, tar):
        index = -1
        left, right = 0, len(b_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if b_list[mid] == tar:
                index = mid
                left = mid + 1
            elif b_list[mid] > tar:
                right = mid - 1
            else:
                left = mid + 1
        return index

    results = [-1, -1]
    results[0] = find_first(nums, target)
    results[1] = find_last(nums, target)
    return results

test = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5]
print(search_range(test, 1))





# My messy first attempt.  See if target is in array.  If it's not, return [-1, -1].  If it is, work to the left from
# where the target was found and find the left most limits, then work to the right finding the limit of the target range.

# def search_range(nums: list[int], target: int) -> tuple[int, int]:
#     left, right, pivot = 0, len(nums) - 1, None
#
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             pivot = mid
#             # testing to see if the pivot is at the beginning or end of the array, if so set the bottom or upper limits
#             # of the range to that number
#             b_lim = pivot if pivot == 0 else None
#             u_lim = pivot if pivot == len(nums)-1 else None
#
#             # if the lower limit hasn't been defined, find it:
#             left, right = 0, pivot - 1
#             while not type(b_lim) == int:
#                 mid = (left + right) // 2
#                 if nums[mid] == target and nums[mid-1] < target:
#                     b_lim = mid
#                 elif nums[mid] == target and nums[mid-1] == target:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#
#             # if the upper limit hasn't been defined, find it:
#             left, right = pivot + 1, len(nums) - 1
#             while not type(u_lim) == int:
#                 mid = (left + right) // 2
#                 if nums[mid] == target and nums[mid + 1] > target:
#                     u_lim = mid
#                 elif nums[mid] == target and nums[mid + 1] == target:
#                     left = mid + 1
#                 else:
#                     left = mid + 1
#
#             return b_lim, u_lim
#
#         # if target wasn't found yet, adjust left/right pointers until it's found, else return [-1,-1]
#         elif target > nums[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1, -1



test_ar = [1, 2, 4, 4, 5, 6]
print(search_range(test_ar, 4))
