"""
Solution Method:
- initial condition is x/2
    - multiple value by itself and compare to x
    - if value is greater than x, decrease test value
    - if value is less than x, increase test value
        - increment/decrement is proportional to different

"""

from math import floor


def mySqrt(target):
    tolerance = .1
    # if target == 0:
    #     return 0
    # else:
    result = target / 2
    prev_result = 0
    while abs(result - prev_result) > tolerance:
        prev_result = result
        result = (prev_result + target/prev_result) / 2
    return result

print(mySqrt(8))
print(mySqrt(4))
print(mySqrt(1))
print(mySqrt(0))
