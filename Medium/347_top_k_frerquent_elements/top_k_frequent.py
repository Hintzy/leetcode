"""
Given an integer array nums and an integer k, return thek most frequent elements.
You may return the answer in any order.

Test/edge cases:
- single element, k = 1
- one unique num, multiple elements of same type, k = 1
- multiple unique elements, k = max
- multiple unique, k = 1
- multiple unique, k != 1 or max (somewhere in between)

Logic:
- Create hashmap that counts amount of elements of top in array (histogram)
"""

from ds_templates import test_series as ts


def top_k_freq_sort(nums: list[int], k: int) -> list[int]:
    histo = {}
    for num in nums:
        histo[num] = histo.get(num, 0) + 1
    lst = [(freq, num) for (num, freq) in histo.items()]
    lst.sort(reverse=True)
    # lst = [num for (freq, num) in lst]
    return lst[:k]


nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]
# print(top_k_freq_sort(nums, 4))


def top_k_freq_bucket(nums: list[int], k:int) -> list[int]:
    histo, res = {}, []
    bucket = [[] for _ in range(len(nums) + 1)]

    for num in nums:
        histo[num] = histo.get(num, 0) + 1
    for key in histo:
        bucket[histo[key]].append(key)

    print(histo)
    for i in range(len(nums), 0, -1):
        for n in bucket[i]:
            res.append(n)
            if len(res) == k:
                return res



nums_bucket = [1]
print(top_k_freq_bucket(nums_bucket, 1))
