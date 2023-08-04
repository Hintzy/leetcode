from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class LinkedList:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return f'LinkedList[{self.root}]'

    def __iter__(self):
        return (x for x in self.root)

    def list_to_SLL(self, a_list):
        if not a_list:
            return None
        head = Node(a_list[0])
        self.root = head
        curr = head
        for num in a_list[1:]:
            curr.next = Node(num)
            curr = curr.next
        return head


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None
    new_head = Node(head.val)
    list_map = {head: new_head}
    new_curr, curr = new_head, head.next
    while curr:
        new_curr.next = Node(curr.val)
        new_curr = new_curr.next
        list_map[curr] = new_curr
        curr = curr.next
    new_curr, curr = new_head, head
    while curr:
        new_curr.random = list_map[curr.random]
        new_curr, curr = new_curr.next, curr.next

    return new_head





list1 = [0, 1, 2, 3, 4, 5]
LL1 = LinkedList()
LL1.list_to_SLL(list1)
print(LL1)
