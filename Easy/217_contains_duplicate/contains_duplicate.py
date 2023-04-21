list_1 = []
list_2 = [1]
list_3 = [1, 1]
list_4 = [2, 1, 1]
list_5 = [1, 2, 3]
list_6 = [1, 2, 3, 3]
lists = [list_1, list_2, list_3, list_4, list_5, list_6]


def containsDuplicate(nums: list[int]) -> bool:
    seen = {}
    for num in nums:
        try:
            seen[num]
        except KeyError:
            seen[num] = seen.get(num, 1)
        else:
            return True
    return False

for i, l in enumerate(lists):
    print(f'Test Case {i}:', containsDuplicate(l))