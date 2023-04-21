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

"""
Function counts the length of the list by traversing it once.  Then traverses the list again len - n to remove that node.
"""

def remove_nth(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head is None:
        return None
    length, current = 0, head
    while current is not None:
        length += 1
        current = current.next

    current = head
    lim = length - n
    if lim == 0:
        head = current.next
        return head
    while lim != 1:
        current = current.next
        lim -= 1
    current.next = current.next.next

    return head

# print(remove_nth(linked_1.head, 2))


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head

sol = Solution()
print(sol.removeNthFromEnd(linked_1.head, 10))
