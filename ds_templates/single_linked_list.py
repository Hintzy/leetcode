class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}, {self.next}'


class LinkedList:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return f'LinkedList[{self.root}]'

    def __iter__(self):
        return (x for x in self.root)

    def list_to_SLL(self, a_list):
        head = ListNode(a_list[0])
        self.root = head
        curr = head
        for i, num in enumerate(a_list[1:]):
            curr.next = ListNode(num)
            curr = curr.next
        return head

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

LL1 = LinkedList()
LL1.list_to_SLL(list_1)
print(LL1)
