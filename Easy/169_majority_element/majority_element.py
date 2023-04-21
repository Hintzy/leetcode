n1 = [2,2,1,1,1,2,2]

def majorityElement(nums: list[int]) -> int:
    num_count = {}
    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1
        # num_count.setdefault(num, 0)
        # num_count[num] += 1
        if num_count[num] > (len(nums) // 2):
            return num

def majorityElement2(nums: list[int]) -> int:
    sol = None
    cnt = 0
    for i in nums:
        if cnt == 0:
            sol = i
        cnt += (1 if i == sol else -1)
    return sol

# print(majorityElement(n1))

print(majorityElement2(n1))