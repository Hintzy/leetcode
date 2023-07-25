"""
Problem logic:

The first solution that comes to mind is one that would have time complexity of O(n^2).

Create a stack that takes values one at a time from 'height'.  Each item that's added to the stack has a loop that
runs through every other item in the stack calculating the maximum area based on that current state of the stack.
(max_area, min_val)

If height = 0 the stack is reset.  Iterate through the full list 'heights'.  The worst case solution would be n^2 if
there are no zeros present in 'height'.
"""
"""
def largest_rect(heights: list[int]) -> int:
    stack, max_area = [], float('-inf')
    for num in heights:
        if num == 0:
            stack = []
        else:
            stack.append(num)
            min_val = float('inf')
            for i, val in enumerate(stack[::-1]):
                width = i + 1
                min_val = min(min_val, val)
                max_iter = min_val * width
                max_area = max(max_area, max_iter)
    return max_area

test_1 = [5, 7, 0, 1, 1, 9]
print(largest_rect(test_1))
"""

"""
Neetcode's logic, my code. 

Populate
"""

from ds_templates import test_series
from test_cases import cases


def largest_rect(heights: list[int]) -> int:
    stack, max_area = [], 0
    for i, height in enumerate(heights):
        if i == 0:
            stack.append([i, height])
        elif height > heights[i-1]:
            stack.append([i, height])
        elif height == 0:
            while stack:
                j, val = stack.pop()
                area = (i - j) * val
                max_area = max(max_area, area)
        elif height < heights[i-1]:
            while stack and height < stack[-1][1]:
                j, val = stack.pop()
                area = (i - j) * val
                max_area = max(max_area, area)
            if not stack:
                stack.append([j, height])
            elif height == stack[-1][1]:
                stack.append([i, height])
            else:
                stack.append([j, height])
    for i, height in stack:
        area = (len(heights) - i) * height
        max_area = max(max_area, area)

    return max_area


# test_1 = [4,2,0,3,2,4,3,4]
# print(largest_rect(test_1))
test_series.test_series(largest_rect, cases)
