"""
No inherent obvious pattern in the output.

Perform calculation on n
If the result is 1, return true
If result is anything else:
    Increment counter by 1
    If counter is less than limit:
        Perform calculation on result

"""

# Iterative solution
def isHappy_1(n: int): # -> bool:
    def calc(num):
        num_tot = 0
        for i in str(num):
            num_tot += int(i) ** 2
        return num_tot

    count = 0
    res = calc(n)
    while count < 101:
        if res == 1:
            return True
        count += 1
        res = calc(res)
    return False

# Recursive solution
def isHappy_2(n: int, c: int): # -> bool:
    if n == 1:
        return True
    if c > 100:
        return False
    tot = 0
    for i in str(n):
        tot += int(i) ** 2
    return isHappy_2(tot, c+1)

print(isHappy_1(19))
print(isHappy_2(19, 0))