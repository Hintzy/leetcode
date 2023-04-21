"""
Since the list will be provided in ascending order, a binary search can be performed on the list to provide a BST.
This would consist of finding the middle element of the list and returning that node. The subsequent
operations would perform the same 'find middle node' function on the left/right portions of the list, until all nodes
are exhausted.

This operation could be performed either directly to the linked list, or by first converting the linked-list to an
array. Converting the linked-list to an array first would take more time and memory, but makes the operations of finding
the middle node and partitioning the list into left/right much easier since there are built in operations for it.
Performing the operations directly to the linked list is trickier.

If the SLL is converted to an array, the middle of the list can be found by setting pointers to the first and nth element
of the array, and dividing the indices by 2 to find a middle value. The function would then perform recursively on the
left partition (0 to mid-1) and right partition (mid+1 to n) to exhaust all the list elements. Everytime a "middle" is
found of a partition, a ListNode is created with the value of the array element.  The center of the left partition is
assigned to listnode.left, and the same for listnode.right.

If the SLL is dealt with directly, the middle of the list can be found with a two pointer approach (slow/fast).  Slow
moves one node at a time, while fast moves two.  Once the fast pointer reaches end of list, the slow node is returned
as the center. To determine the right partition is simple as the node after middle can be returned. The left partition is
created by making the node immediately to the left of middle have a None for next, and then head is returned. The base
condition returns none.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}, {self.next}'

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return f'LinkedList[{self.head}]'

    def populate(self, a_list):
        if not a_list:
            return None
        self.head = ListNode(a_list[0])
        curr = self.head
        for num in a_list[1:]:
            curr.next = ListNode(num)
            curr = curr.next
        return self.head



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val})'

class BST:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return f'BST[{self.root}]'


def find_mid(node):
    slow = node
    fast = node
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    if prev:
        prev.next = None
    return slow

def LL_to_BST(node):
    if not node:
        return None
    if not node.next:
        return TreeNode(node.val)
    middle = find_mid(node)
    root = TreeNode(middle.val)
    root.right = LL_to_BST(middle.next)
    middle.next = None
    root.left = LL_to_BST(node)
    return root

list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
LL1 = LinkedList()
LL1.populate(list_1)
ll1_head = LL1.head
BST1 = BST()
BST1.root = LL_to_BST(ll1_head)