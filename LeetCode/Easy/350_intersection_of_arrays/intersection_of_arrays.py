n = [1, 2, 3, 4, 5, 6, 7, 8]
m = [4, 5, 6, 7, 4, 9, 10]

"""
Determine the lengths of two lists: 
    use the shorter list of the two as the primary iteration list

Iterate through the shorter list using a standard for loop:
    Compare letter against longer list using a counter to the first item.
        - If they're not equal, check hashmap for occurrence of item.  If it's in the hashmap, pop the first index If not in hashmap, add value from target list
            into a hashmap with "num": list[indices] for later lookup, finally increment counter to move to next itme.
        - If letter from longer equals shorter, 
 
"""

def intersect(nums1: list[int], nums2: list[int], i: int=0) -> list[int]:
    result = []
    if not nums1 or not nums2:
        return result
    nums2_dict = {num: [i for i, n in enumerate(nums2) if n == num] for num in set(nums2)}
    for num in nums1:
        try:
            if nums2_dict[num]:
                result.append(num)
                nums2_dict[num].pop()
        except KeyError:
            continue
    return result




        #     if nums1[i] in nums2:
        #         result.append(nums2.pop(i))
        # except IndexError:
        #     return result
        # else:
        #     return intersect(nums1, nums2, i+1)

print(intersect(n, m))