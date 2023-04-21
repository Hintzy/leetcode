"""
Cases:
    1. reg number
    2. neg number
    3. empty string
    4. string starting with letters
    5. string starting with letters with - before the number
    6. string starting with - then letters, then a number
    7. letters occurring after the end of the number

"""

def myAtoi(s: str) -> int:

# Converts input to string (if it isn't already) and removes leading/trailing whitespace.
    s = str(s).strip()
    sign = 1
    if len(s) == 0:
        return 0
    if s[0] == '-' or s[0] == '+':
        if len(s) == 1:
            return 0
        sign = -1 if s[0] == '-' else 1
        s = s[1:]
    num = ''
    while s[0].isdigit() and len(s) != 1:
        num = num + s[0]
        s = s[1:]
    if s[0].isdigit():
        num = num + s[0]
    if len(num) == 0:
        return 0
    else:
        num = int(num) * sign
        if num > (2 ** 31) - 1:
            return (2 ** 31) - 1
        elif num < -2 ** 31:
            return -2 ** 31
        else:
            return num
    
"""
    s = str(s).strip()
    # A default positive value is given, which will only be changed if a '-' is found before the first digit below. 
    sign = 1
    if len(s) == 0:
        return 0
    # Cycles through first character is string until a digit found. If char is '-', sign is changed to -1.
    if s[0] == '-':
        sign = -1
        s = s[1:]
    # Appends digits to an empty string until a non-digit is encountered.
    num = ''
    while s[0].isdigit() and len(s) != 1:
        num = num + s[0]
        s = s[1:]
    if s[0].isdigit():
        num = num + s[0]
    # If letters came before the number, len of string will be 0, otherwise the number is multiplied by the sign and
    # returned.
    if len(num) == 0:
        return 0
    else:
        num = int(num) * sign
        if num > (2 ** 31) - 1:
            return (2 ** 31) - 1
        elif num < -2 ** 31:
            return -2 ** 31
        else:
            return num
"""
    



str_1 = 502
str_2 = -502
str_3 = "-91283472332"

print(myAtoi(str_1))
print(myAtoi(str_2))
print(myAtoi(str_3))