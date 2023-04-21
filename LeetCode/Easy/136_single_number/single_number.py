n_1 = [2, 2, 1]

def single_number(nums: list[int]) -> int:
    occurred = {}
    for num in nums:
        if num in occurred:
            del occurred[num]
        else:
            occurred[num] = None
    for key in occurred.keys():
        return key

print(single_number(n_1))