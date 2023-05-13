"""
Problem statement:

The problem states that a dividend and a divisor are given and a function that performs division must be developed
without the use of multiplication, division, or mod operators. The answer is to be truncated such that any remainder is
discorded, effectively mimicing a floor division function.

A brute force solution that can be offered that would be inefficient would be to increment the divisor by itself using
+= and each time compare the current sum to the dividend.  If the sum exceeds the dividend then return the answer,
otherwise increment a counter. This solution would be inefficient on its own, but in the absence of a multiplication or
division operation will be the basis of the algorithm solution.
The 'divide_long' function essentially takes the divide_small function and performs long division by parsing through the

The solution algorithm first determines the sign of the ultimate answer, so that the signs can be disposed of while the
magnitude of the solution is calculated.

The algorithm then performs a similar function to the brute force algorithm above, making constant subtractions of the
divisor from the dividend, except instead of continuously subtracting the same divisor, a bitwise manipulation of the
divisor is performed after each subtraction, effectively increasing the divisor by a factor of 2. As long as the new
divisor isn't larger than the current remaining dividend, it continues to grow. The divisor grows exponentially by a
factor of 2. The "number of divisors" is tracked along with the growing divisor by performing the same bitwise
manipulation. Once the current divisor exceeds the value of the dividend, it is reset to the original divisor size and
the process is repeated until the base divisor cannot be subtracted from the divident anymore.  At which point the
result is returned.
"""

def divide(num: int, den: int):
    positive = (num < 0) is (den < 0)
    num, den = abs(num), abs(den)
    res = 0

    while num >= den:
        curr_den, den_count = den, 1
        while num >= curr_den:
            num -= curr_den
            res += den_count

            curr_den = curr_den << 1
            den_count = den_count << 1

    if not positive:
        res = -res

    return min(max(-2147483648, res), 2147483648), num

