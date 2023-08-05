from typing import Optional
from ds_templates import single_linked_list as sll


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: list) -> ListNode:

    def find_min(lists:list) -> int or None:
        ind, min_val = None, float('inf')
        for i, head in enumerate(lists):
            if head:
                min_val = min(min_val, head.val)
                if head.val == min_val:
                    ind = i
        return ind

    merged = ListNode()
    curr = merged

    while True:
        list_ind = find_min(lists)
        if list_ind is None:
            break
        curr.next = lists[list_ind]
        lists[list_ind] = lists[list_ind].next # assign min_node to the node identified as min
        curr = curr.next

    return merged.next


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

all = sll.LinkedList()
nl1 = all.list_to_SLL(list1)
nl2 = all.list_to_SLL(list2)
nl3 = all.list_to_SLL(list3)
sll_lists = [nl1, nl2, nl3]

print(mergeKLists(sll_lists))