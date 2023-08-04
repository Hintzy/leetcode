"""
Solution:
1. check if either list is empty, if so, return the other list
    (Note: if the other list is also empty (i.e. 'None') then returning the other list will still be correct)
2. perform a loop while both lists have values, taking the lesser head value, setting that as the head.next value of the
    merged list, and advancing the current node of the merged list as well as the node of the list the value was taken
    from
3. once one of the lists is exhausted (i.e. current head value is 'None') then the head of the other list is set as the
    next node and the head of the merged lists is returned
"""

from ds_templates import test_series
from test_cases import cases


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}, {self.next}'


def create_linked_list(head):
    if not head:
        return None
    head_node = ListNode(head[0])
    current_node = head_node
    for num in head[1:]:
        new_node = ListNode(num)
        current_node.next = new_node
        current_node = new_node
    return head_node


def print_lists(l1, l2, l3):
    print(f'list 1 - {l1}, list 2 - {l2}, merged - {l3}')


def mergeTwoLists_v1(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    l1_cur = list1
    l2_cur = list2

    if l1_cur.val <= l2_cur.val:
        merged_head = l1_cur
        l1_cur = l1_cur.next
    else:
        merged_head = l2_cur
        l2_cur = l2_cur.next

    current_node = merged_head

    while l1_cur and l2_cur:
        if l1_cur.val <= l2_cur.val:
            current_node.next = l1_cur
            l1_cur = l1_cur.next
        else:
            current_node.next = l2_cur
            l2_cur = l2_cur.next
        current_node = current_node.next

    if not l1_cur:
        current_node.next = l2_cur
    else:
        current_node.next = l1_cur

    return merged_head


def mergeTwoLists_v2(l1: ListNode, l2: ListNode) -> ListNode:

    # if either of the lists are initially empty return the other list as the output
    if not l1:
        return l2
    if not l2:
        return l1

    # guaranteed that both lists have nodes in them to  perform the following loop while both lists still have elements
    # step 1 - create the head of the merged linked list

    if l1.val <= l2.val:
        merged_head = l1
        l1 = l1.next
    else:
        merged_head = l2
        l2 = l2.next

    curr = merged_head

    # step 2 - iterate through the lists, appending the lesser of the two values to the merged head
    # curr keeps track of the node we're currently working on, preserving the merged list header
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # step 3 - loop should have exhausted through the smaller of the two lists, leaving only one with remaining elements
    if not l1:
        curr.next = l2
    else:
        curr.next = l1

    return merged_head

# _________ Testing parameters __________
"""
list1 = [1, 4, 5, 9]
list2 = [2, 4, 6, 7]
list3 = []
list4 = [1]

ll1_head = create_linked_list(list1)
ll2_head = create_linked_list(list2)

print(f'linked list1 - {ll1_head}')
print(f'linked list2 - {ll2_head}')
print(f'Merged list - {mergeTwoLists_v2(ll1_head, ll2_head)}')
"""

test_series.test_series(mergeTwoLists_v2, cases)
