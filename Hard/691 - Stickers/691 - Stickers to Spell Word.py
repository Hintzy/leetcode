stickers = ['with', 'example', 'science']
target = 'thehat'

for word in stickers:
    in_common = {}
    common_dict = {}
    for letter in word:
        if letter in set(target):
            in_common.setdefault(letter, 0)
            in_common[letter] = target.count(letter)
        common_dict.setdefault(word, {})
        common_dict[word] = in_common
    for key, val in common_dict.items():
        item_tot = 0
        for item in val:
            item_tot += val

    # print(f'{word} - {in_common}')
    # print(common_dict)
