"""
Given the head of a linked list and an integer 'val', remove all the nodes of hte linked list that has node.val == val,
return the new head

Cases:
1. no values in list matching val
2. all values in list matching val
3. header has the val
3a. header has the val with multiple in a row
4. tail has the val
5. generic list with some vals

Approach:
    - Since the header might have to be deleted, we need a pointer to the header so it can be reassigned
        pre = self, pre.next = head
    - While the incoming node is not None:
        while pre.next is not None:
        cur = pre.next
        if cur.value = arguement
            pre.next = cur.next
            continue
        pre = pre.next



"""

from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}, {self.next}'

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return f'{self.head}'

    def populate(self, lst):
        self.head = ListNode(lst[0])
        current = self.head
        for num in lst[1:]:
            new_node = ListNode(num)
            current.next = new_node
            current = current.next

    def remove_val(self, num):
        head = self.head
        prev = ListNode(0, head)

        while head and head.val == num:
            prev, head = prev.next, head.next

        current = head
        while current:
            if current.val == num:
                prev.next = current.next
                current = current.next
            else:
                prev = prev.next
                current = current.next

        return head

case_1 = [6, 6, 1, 2, 6, 3, 4, 5, 6]
val_1 = 6

case_2 = [8, 8, 8, 8, 8]
val_2 = 8

case_3 = [1, 2, 3, 4, 5, 6]
val_3 = [1]

case_4 = [1, 1, 1, 2, 3, 4, 5, 6]
val_4 = [1]

case_5 = [1, 1, 1, 2, 3, 4, 5, 6]
val_5 = [6]

case_6 = [1, 6, 1, 2, 6, 4, 5, 6]
val_6 = [6]

linked_1 = LinkedList(case_1[0])
linked_2 = LinkedList(case_2[0])
linked_3 = LinkedList(case_3[0])
linked_4 = LinkedList(case_4[0])
linked_5 = LinkedList(case_5[0])
linked_6 = LinkedList(case_6[0])

linked_1.populate(case_1)
linked_2.populate(case_2)
linked_3.populate(case_3)
linked_4.populate(case_4)
linked_5.populate(case_5)
linked_6.populate(case_6)

print(linked_1.remove_val(6))
# print(linked_1.remove_val(linked_1.head, 1))
