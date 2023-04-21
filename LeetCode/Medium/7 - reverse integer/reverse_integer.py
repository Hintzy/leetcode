# def reverse(x: int) -> int:
# """ Given a signed 32-bit integer, x, return x with its digits reversed. If value goes outside the range of 32-bit
# integer range (-2 ^ 31, (2 ^ 31) - 1), then return 0"""
#     print(x)
#     bin_x = bin(x)
#     print(bin_x)
#     bin_strip = ''.join([x for x in bin_x if x.isdigit()])
#     print(bin_strip)
#     bin_rev = bin_strip[::-1]
#     print(bin_rev)
#     bin_rev_red = bin_rev[1:]
#     print(bin_rev_red)
#     print(int(bin_rev_red, 2))

def reverse(x: int) -> int:
    sign = 1 if x >= 0 else -1
    x = abs(x)
    # rev = 0
    # while x > 0:
    #     rev = rev * 10 + x % 10
    #     x //= 10
    # rev *= sign
    rev = sign * int(str(x)[::-1])
    if rev < -2 ** 31 or rev > 2 ** 31 - 1:
        return 0
    return rev

def reverse2(x: int) -> int:
    sign = 1 if x >= 0 else -1
    x = abs(x)
    rev = 0
    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10
    rev *= sign
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    return rev


print(reverse(123))
print(reverse(123))


