"""
The brute force solution to this problem will take the form of a recursive function with a helper function. The helper
 function will calculate the volume of water based on two selected elements from the array.  The outer function will
 go from 0 to n for the right element, and 0 to right.
"""

heights = [x for x in range(20)]

def maxArea_brute(height: list[int]) -> int:
    n = len(height)
    max_vol = float('-inf')
    for right in range(1, n):
        for left in range(right):
            min_h = min(height[left], height[right])
            w = right - left
            vol = min_h * w
            max_vol = max(vol, max_vol)
    return max_vol

"""
A sliding window approach could be implemented with pointers the move the left and right bounds based on the distance 
from the current bounds and the value found at each step.

i starts at 0
j starts at end of array

1. calculate volume
2. whichever height is smaller (i or j), increments inward until a larger value is found, check volume with that larger value 
    - if larger volume, set that as the new volume max, otherwise keep current volume
    - regardless of if volume is larger or not, continue to increment the smaller of the two bound heights until lower = upper
"""


# Code from March 2023
"""
def maxArea(height: list[int]):

    def volume(i, j, height):
        return (j - i) * (min(height[i], height[j]))

    # set i to point to first array element and j to point to last array element. Calculate the volume using these bounds
    i = 0
    j = len(height) - 1
    max_vol = volume(i, j, height)

    # while the left pointer is less than the right pointer...
    while i < j:
        # move the pointer with the smaller of the two values inward until a larger value is found
        if height[i] <= height[j]:
            while height[i+1] < height[i]:
                i += 1
            i += 1
            max_vol = max(volume(i, j, height), max_vol)
        else:
            while height[j-1] < height[j]:
                j -= 1
            j -= 1
            max_vol = max(volume(i, j, height), max_vol)
    return max_vol

height_1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(maxArea(height_1))
"""

# Revisiting problem in June 2023 with a fresh attempt

# set a helper function to calculate volume of a given pair of indices
# initialize volume as 0, define a function that will calculate volume
# while j > i, move smaller pointer inward until a greater value than current is found, calculate volume as max between
# current max and current calculated.  Continue process until j passes i


def maxArea(height: list[int]) -> int:

    def volume(i: int, j: int, lst: list[int]):
        vol = (j - i) * (min(lst[i], lst[j]))
        return vol

    i, j = 0, len(height) - 1
    max_vol = max(0, volume(i, j, height))

    while i < j:
        if height[i] <= height[j]:
            cur = height[i]
            while height[i+1] <= cur and i < j:
                i += 1
            i += 1
            max_vol = max(max_vol, volume(i, j, height))

        else:
            cur = height[j]

            while height[j-1] <= cur and i < j:
                j -= 1
            j -= 1
            max_vol = max(max_vol, volume(i, j, height))

    return max_vol

