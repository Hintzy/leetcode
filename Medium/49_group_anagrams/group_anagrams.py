from ds_templates import test_series as ts
from test_cases import tests

"""
1) Parse through list word by word, sorting each word to obtain a 'key'
2) Use sorted word as key for 'anas' and the value is a list with words within.
3) One full list has been parsed, iterate through anas.values() and append to results list 
"""

def group_anagrams(strs: list[str]) -> list[list[str]]:
    anas, res = {}, []
    for word in strs:
        key = ''.join(sorted(word))
        anas.setdefault(key, [])
        anas[key].append(word)
    for lst in anas.values():
        res.append(lst)
    return res

strs1 = ['stuff', 'fusft', 'ffust', 'cats', 'stac', 'atcs', 'dogg', 'god']
print(group_anagrams(strs1))
