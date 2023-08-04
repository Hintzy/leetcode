from ds_templates import single_linked_list as sll
cases = []

lists = [
    ([0, 2, 4, 6, 8], [1, 3, 5, 7]),
    ([2], [1]),
    ([0, 0, 1, 1], [5, 6, 7]),
    ([], [1]),
    ([], []),
    ([0], [0]),
    ]


def LL(l):
    return sll.LinkedList().list_to_SLL(l)


for pair in lists:
    l1 = pair[0]
    l2 = pair[1]
    l3 = sorted(l1 + l2)
    cases.append({
        'input': {
            'l1': LL(l1),
            'l2': LL(l2),
        },
        'output': LL(l3)
    })

print(cases)
