def findMedian(nums1: list[int], nums2: list[int]) -> float:
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    # find the middle of smaller array
    l, r = 0, len(A) - 1
    while True:
        midA = (l + r) // 2
        midB = (half - midA) - 2
        if total % 2 == 1:
            if B[half - midA] >= A[midA] and A[midA+1] >= B[half - (midA+1)]:
                return min(B[half - midA], A[midA+1])
            elif B[half - midA] < A[midA]:
                r = midA - 1
            else:
                l = midA + 1
        else:
            if B[half - midA] >= A[midA] and A[midA+1] >= B[half - (midA+1)]:
                lower = max(B[half - (midA+1)], A[midA])
                upper = min(B[half - midA], A[midA+1])
                return (lower + upper) / 2
            elif B[half - midA] < A[midA]:
                r = midA - 1
            else:
                l = midA + 1

num1 = [1, 3, 4, 5]
num2 = [2, 5, 7, 8]

print(findMedian(num1, num2))
