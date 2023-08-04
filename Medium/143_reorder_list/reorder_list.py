from ds_templates import single_linked_list as sll
from typing import Optional

LL1 = sll.LinkedList()
LL1.list_to_SLL([0, 1, 2, 3, 4, 5, 6])



def reorder_list(head: sll.ListNode) -> sll.ListNode:
    curr = head
    stack = []
    while curr.next:
        curr = curr.next
        stack.append(curr.val)
    curr, ind = head, -1
    while stack:
        curr.next = sll.ListNode(stack.pop(ind))
        curr = curr.next
        ind = 0 if ind == -1 else -1
    return head


print(reorder_list(LL1.root))
