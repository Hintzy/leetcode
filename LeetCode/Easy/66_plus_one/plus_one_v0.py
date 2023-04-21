def plusOne(digits):
    # for num in digits:
    digits_str = ''
    for item in digits:
        digits_str += str(item)
    digits_str = int(digits_str)
    digits_str += 1
    digits_str = list(str(digits_str))
    return digits_str

digits_1 = [4, 3, 2, 1]
digits_2 = [1, 2, 3, 4]
digits_3 = [1, 2, 4, 9]


print(plusOne(digits_1))
print(plusOne(digits_2))
print(plusOne(digits_3))
