"""
Solution method:
1. convert string to a list of characters
2. use list comprehension to create a list of values
3. scan through list looking for an increase in value instead of decrease
    - where the increase occurs, merge those two values to perform the subtraction
4. perform sum on the resulting list
"""



rom_num = 'III'
rom_num1 = 'LVIII'
rom_num2 = 'MCMXCIV'


def romanToInt(s: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    chars = list(s)
    vals = [values[let] for let in chars]
    for i, val in enumerate(vals):
        try:
            val < vals[i + 1]
        except IndexError:
            pass
        else:
            if val < vals[i + 1]:
                vals[i] = vals[i + 1] - vals[i]
                vals.pop(i + 1)
    return sum(vals)


print(romanToInt(rom_num))
print(romanToInt(rom_num1))
print(romanToInt(rom_num2))
