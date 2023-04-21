from test_cases import cases, evaluate_cases

"""
Potential edge cases:
1. empty list
2. list with one number
    - one number and it's not zero
    - one number and it is zero
3. list with zero at beginning
4. list with zero at end
5. regular dispersed list with several zeros
6. list with multiple zeros next to one another
"""

def move_zeroes(nums: list) -> None:
    i = 0
    for num in nums:
        if num == 0:
            nums.append(nums.pop(i))
        else:
            i += 1

evaluate_cases(move_zeroes, cases)

