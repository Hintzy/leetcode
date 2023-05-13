"""
The object of this problem is to take a string of numbers, which correspond to letters on a touch-tone phone keypad,
and return all the possible letter permutations that can be created with those numbers.  Digits are in range of 2-9,
and the length of the input string is between 0 and 4 (inclusive) characters.

Cases:
1. empty string
2. string of a single char
3. string of 4 chars
4. string of random chars
5. string of all same chars

The solution to this method needs to accept a string of unknown length (though we know it is maximum 4 chars), and
iterate through each letter, and create all permutations with the letters of the following character.
"""

"""
The following is an iterative method that uses a for loop and indices to traverse through the letters.  Not a recusive
method.
"""
def letter_combos(digits: str) -> list[str]:
    ltr_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    raw = []
    res = []
    cur = ''
    for num in digits:
        raw.append(ltr_map[num])

    # permutations = 1
    # for lst in raw:
    #     permutations *= len(lst)
    #     print(permutations)


#     # for num in
#     for i in range(len(raw)):
#         for j in range(len(raw[i])):
#             print(f'2nd level {i, j}')
#             for k in range(len(raw)):  # this loops through each of the lists and should be the lowest level
#                 print(f'3rd level: {i, j, k}')
#
#
# str_1 = '2'
# str_2 = '23'
# str_3 = '234'
#
# print(letter_combos(str_1))
# print(letter_combos(str_2))
# print(letter_combos(str_3))

# ___________________________________________________________________________________________________________

"""
This is a recursive attempt at the same problem.  

The solution consists of an inner and outer function.  The outer function takes the string of numbers as an input.  The 
output of the outer function is the list of string permutations.  Inner function takes a base string to concatenate, 
and a string to add to it.
"""

def letter_combos_recurse_2(digits: str) -> list[str]:
    if not digits:
        return []

    ltr_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    res = []

    def recurse(a_str, next_digs):
        if not next_digs:
            res.append(a_str)
            return

        for let in ltr_map[next_digs[0]]:
            recurse(a_str + let, next_digs[1:])

    recurse('', digits)
    return res

print(letter_combos_recurse_2('23'))