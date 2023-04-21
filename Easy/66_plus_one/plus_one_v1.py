"""
Solution Method:
while last digit equals 9, make last digit a zero
otherwise the next after last digit 1
"""

def plusOne(digits):
    i = -1
    while abs(i) != len(digits):
        if digits[i] == 9:
            digits[i] = 0
            i -= 1
        else:
            digits[i] += 1
            return digits
    if digits[i] == 9:
        digits[i] = 0
        digits.insert(0, 1)
    else:
        digits[i] += 1
    return digits


digits_1 = [9, 9, 9, 9]
digits_2 = [9, 8, 9, 9]
digits_3 = [9, 9, 0, 0]
digits_4 = [9, 9, 9, 9, 9]


print(plusOne(digits_1))
print(plusOne(digits_2))
print(plusOne(digits_3))
print(plusOne(digits_4))
