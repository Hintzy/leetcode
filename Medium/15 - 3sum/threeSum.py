def three_sum_brute(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets of the array elements that sum to zero.  This version of the function is a brute force
    method, which tests every combination of i, j, k-th elements in the array.  Time complexity O(n^3) (unacceptable!)
    """
    n = len(nums)
    res = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if i == k or j == k:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    ans = sorted([nums[i], nums[j], nums[k]])
                    if ans in res:
                        continue
                    else:
                        res.append(ans)


def three_sum_hash(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets of the array elements that sum to zero.  This version of the function uses a hashmap of
    all the values within the list to find the complement of the sum of the first two numbers identified.
    E.g. if nums[i] == 1 and nums[j] == 1 (i != j), then search the hashmap for a value -2.  If it exists, the triplet
    is compared against the list of found triplets so far.  If it's not found yet, it's stored
    """
    n = len(nums)
    res = []
    hm = {}
    for i, num in enumerate(nums):
        if num in hm:
            hm[num].append(i)
        else:
            hm[num] = [i]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            complement = -(nums[i] + nums[j])
            if complement in hm:
                unique = [x for x in hm[complement] if x != i and x !=j]
                if unique:
                    res_check = sorted([nums[i], nums[j], complement])
                    if res_check in res:
                        continue
                    res.append(res_check)
    return res

def three_sum_pointer(nums: list[int]) -> list[list[int]]:
    # create empty list to store the unique triplets and sort the list (O(n log(n))
    res = []
    nums.sort()

    # start a loop through all elements in nums minus the last two, as the index will be used as the lower end of the
    # triplet, and we will need two elements after every element picked up by the loop.
    for i in range(len(nums)-2):
        # skip any leading duplicates that occur starting at the beginning of the list
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # establish l and r pointers that occur after i
        l, r = i + 1, len(nums) - 1
        # find possible permutations summing to 0 using the (i) iteration as the lower bound, and moving the two
        # pointers ahead of it inward from their starting positions
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                # if a triplet summing to zero is found, append the results list with the triplet, and move both
                # pointers inward to the unique number, accounting for potential index errors
                res.append([nums[i], nums[l], nums[r]])
                while l < len(nums) - 2 and nums[l] == nums[l+1]:
                    l += 1
                while r > l and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res

nums = [-1,0,1,2,-1,-4]
# nums = [0,0,0]
print(three_sum_pointer(nums))