"""
Iterate through list until None.

At each node, check if the value is in seen
    If value in seen, remove duplicate.
        To remove duplicate, keep track of a prev pointer.  If need to reassign, make prev.next = current.next.
        The move on with current = current.next.  Leave prev


    If value not in seen, add to hashmap, move onto next node with prev, current = prev.next, current.next

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

    def delete_duplicates_1(self):
        pre, pre.next, head = self, self.head, self.head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            while b.next and a.val == b.val:
                a.next = b.next
                b = b.next
            if a.val == b.val:
                a.next = b.next
            pre = pre.next
        return self.head


    def delete_duplicates_2(self):
        temp, copy = self.head, self.head
        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
                continue
            temp = temp.next
        return self.head


list_1 = [0, 0, 0, 1, 1, 2, 3, 3, 4, 4]
linked_1 = LinkedList()
linked_1.populate(list_1)
print(linked_1.delete_duplicates_2())


