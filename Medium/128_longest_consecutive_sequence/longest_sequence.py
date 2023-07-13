def longestConsecutive(nums: list[int]) -> int:

    nums_set = set(nums)
    sequences = {}
    longest = 0

    # identify all the starting points of sequences
    for num in nums_set:
        if num - 1 not in nums_set:
            sequences[num] = [num]

    for seq in sequences:
        x = seq + 1
        while x in nums_set:
            sequences[seq].append(x)
            x += 1

    for seq in sequences.values():
        longest = max(longest, len(seq))

    return longest


nums_1 = [0, 1, 2, 3, 4, 7, 8, 9, 15, 16, 17, 19, 21, 23, 100]


print(longestConsecutive(nums_1))
