"""
Write a two pointer approach with pointers moving in from the left/right.

Edge case needs to be solved for each - looking for that first point where it starts to go downwards... or just apply
the same algoritm across....

pointer moving inward with an accumulator variable... pointer is an index number for the 'height' array.
Variables keeping track of current max height for L and R and their index (curr_peak_L & curr_peak_R)

While L < R:
Increment L & R inward, while height[i] is less than curr_peak height for L & R respectively, accumulate onto the
accum_L / accum_R and increment L / R and increment inward.

If/when height[i] >= curr_peak, set the new curr peak and index (nothing needs to be done to the accumulator).

When L = R:


"""


def find_peaks(nums: list[int]) -> list[int]:
    res = []
    if nums[0] > nums[1]:
        res.append(0)
    for i in range(1, len(nums)-1):
        if nums[i-1] <= nums[i] >= nums[i+1]:
            res.append(i)
    if nums[-1] > nums [-2]:
        res.append(len(nums)-1)
    return res

stuff = [5, 3, 4, 3, 5]

print(find_peaks(stuff))
