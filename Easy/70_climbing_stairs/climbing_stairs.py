"""
Solution:
extreme cases:
    list length equals number of steps and all steps are 1: len(list) = n
    list length consists of all 2 steps until equal n len(list) n/2
    or all two steps until and plus 1 len(list) = n/2 + 1   

n = 1
ans = 1
list: [1]
        1c1

n = 2
n = 2
list:  [2], [1, 1]
        1c0   +   2c2


n = 3
n = 3
list: [2, 1], [1, 2], [1, 1, 1]
           2 C 1     +     3c3
n = 4
ans = 5
list: [2, 2], [1, 1, 2]..., [1, 1, 1, 1]
        2 c 0      3 C 2   +     4 c 4

n = 5
list: [2, 2, 1]..., [2, 1, 1, 1]..., [1, 1, 1, 1, 1]
        3 C 1   +    4 c 3    +     1

n = 6
list: [2, 2, 2] ... [2, 2, 1, 1] ... [2, 1, 1, 1, 1] ... [1, 1, 1, 1, 1, 1]
         3 c 0          4 C 2    +         5 C 4         +         6 c 6

n = 7 [2, 2, 2, 1], [2, 2, 1, 1, 1], [2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]
        4 c 1     +     5 c 3       +       6 c 5       +         1
"""

from math import factorial


def ncr(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))



def climbStairs(n: int):
    total = 0
    upper = n+1
    if n <= 2:
        return n
    elif n % 2 != 0:
        lower = int(n/2) + 1
        r = 1
        for i in range(lower, upper):
            total += ncr(i, r)
            r += 2
        return total
    else:
        lower = int(n / 2)
        r = 2
        for i in range(lower, upper):
            total += ncr(i, r)
            r += 2
        return total

print(climbStairs(3))
