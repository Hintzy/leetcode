def removeDuplicates(nums):
    val = nums[0]
    k = 1
    for i, x in enumerate(nums[1:]):
        if x == val:
            nums.append('_')
            nums.remove(val)
        else:
            val = nums[k]
            k += 1
    return k


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = removeDuplicates(nums)
print(f'k = {result[0]}, nums = {result[1]}')

