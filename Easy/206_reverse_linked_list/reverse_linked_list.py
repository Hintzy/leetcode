from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}, {self.next}'


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        return f'{self.head}'

    def populate(self, lst):
        self.head = ListNode(lst[0])
        cur = self.head
        for i in lst[1:]:
            cur.next = ListNode(i)
            cur = cur.next

    # def traverse(self):
    #     if self.head is None:
    #         return None
    #     cur = self.head
    #     def trav(node):
    #         if node.next is None:
    #             return None
    #         return cur.val, cur.next
    #     return trav(cur)

    def reverse_list_it(self):
        """
        Edge cases for empty set and single point
        """
        prev = None
        cur = self.head
        next = cur.next
        while next is not None:
            cur.next = prev
            prev = cur
            cur = next
            next = next.next
        cur.next = prev
        return self.head

    # a recursive solution to reversing a linked list
    def reverse_list_recurse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the current node is None or the next node is None, return the current node
        if not head or not head.next:
            return head

        # Recursively call the function with the next node as the argument
        new_head = self.reverse_list_recurse(head.next)

        # Set the next node's next pointer to the current node
        head.next.next = head

        # Set the current node's next pointer to None
        head.next = None

        # Return the head node (which will be the new head of the reversed list)
        return new_head

    def rev_LL(self) -> Optional[ListNode]:
        if self.head is None:
            return None
        last, cur = None, self.head
        next = cur.next
        while next is not None:
            cur.next = last
            last = cur
            cur = next
            next = cur.next
        cur.next = last
        self.head = cur
        return self.head



# creating a linked list from an array
list_1 = []
LL1 = LinkedList()
LL1.populate(list_1)
print(LL1)
# LL1.rev_LL(LL1.head)
print(LL1.rev_LL())
# print(LL1.reverse_list_recurse(LL1.head))

# fresh attempt at redoing this problem months later

