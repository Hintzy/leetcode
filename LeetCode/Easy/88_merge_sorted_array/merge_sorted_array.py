def merge(nums1, m, nums2, n):
    for i, num in enumerate(nums2):
        nums1[m+i] = num
    nums1.sort()

n1 = [1, 2, 3, 0, 0, 0]
n2 = [8, 9, 10]
merge(n1, 3, n2, 3)
