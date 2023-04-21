def titleToNumber(columnTitle: str) -> int:
    res = 0
    for i, let in enumerate(columnTitle[::-1]):
        val = ord(let) - 64
        val *= (26 ** i)
        res += val
    return res

title_1 = 'A'
title_2 = 'Z'
title_3 = 'AA'
title_4 = 'AZ'
title_5 = 'ZA'
title_6 = 'ZZZZZZZ'
cases = [title_1, title_2, title_3, title_4, title_5, title_6]

for case in cases:
    print(titleToNumber(case))
