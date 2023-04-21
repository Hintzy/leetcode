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

list_1 = [x for x in range(10)]
linked_1 = LinkedList()
linked_1.populate(list_1)


class Solution:
    def swapPairs_me(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize pointers to 1st/2nd nodes
        first, second = self, head

        while first.next and first.next.next:
            # swap first/second nodes
            first.next = second.next
            second.next = first

        # reestablish list head
        head = second

        # reestablish pointers
        first, second = second.next, second.next.next
        # swap newly established nodes
        first.next = first.next.next
        second.next = first
        print(f'head: {head}')
        print(f'first: {first}')
        print(f'second: {second}')

    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

sol = Solution()
print(sol.swapPairs(linked_1.head))