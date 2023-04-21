"""
Edge cases:
0
1
"""

def power_of_three(num):
    if num == 0:
        return False
    result, x = 0, 1
    while abs(result) < abs(num):
        result = 3 ** x
        if result == num:
            return True
        x += 1
    return False

