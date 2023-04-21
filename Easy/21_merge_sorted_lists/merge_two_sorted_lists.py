"""
Solution:
1. create linked lists
2. initialize merged list as empty

loop...
3. if both lists are empty, return current state of merged list
4. bool test to see if both lists are not false
    - if one list is empty, return the current node of other list
3. If both lists have values merged list takes the lesser
    of the head node values
4. repeat until
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'[{self.val}, {self.next}]'


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


def mergeTwoLists(list1, list2):
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



# _________ Testing parameters __________

list1 = [1, 4, 5, 9]
list2 = [2, 4, 6, 7]

list1_head = create_linked_list(list1)
list2_head = create_linked_list(list2)

print(f'ordinary list1 - {list1}')
print(f'ordinary list2 - {list2}')
print(f'linked list1 - {list1_head}')
print(f'linked list2 - {list2_head}')
print(f'Merged list - {mergeTwoLists(list1_head, list2_head)}')
