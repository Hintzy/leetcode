def three_sum_bf(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets of the array elements that sum to zero.  This version of the function is a brute force
    method, which tests every combination of i, j, k-th elements in the array.
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


nums = [-1,0,1,2,-1,-4]
print(three_sum_hash(nums))