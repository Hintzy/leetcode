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
"""


def largest_rect(heights: list[int]) -> int:
    stack = [(0, heights[0])]
    max_area = stack[0][1]
    for i, num in enumerate(heights):
        if i == 0:
            continue
        stack.append((i, num))
        for j, val in stack:
            while num < val:
                ind, curr_val = stack.pop(j)
                area = curr_val * (i - j)
                max_area = max(area, max_area)
    return max_area


test_lab = [1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 0, 1, 2]
print(largest_rect(test_lab))

