class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'[{self.val}, {self.next}]'


class LinkedList:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return f'LinkedList({self.root})'

    def __iter__(self):
        return (x for x in self.root)

    def populate(self, a_list):
        self.root = ListNode(a_list[0])
        curr = self.root
        for num in a_list[1:]:
            new_node = ListNode(num)
            curr.next = new_node
            curr = curr.next

    def list_to_looped_SLL(self, a_list, idx):
        head = ListNode(a_list[0])
        self.root = head
        curr = head
        for i, num in enumerate(a_list[1:]):
            curr.next = ListNode(num)
            if i == idx:
                loop_pointer = curr.next
            curr = curr.next
        curr.next = loop_pointer
        return head

    def has_loop(self):
        seen = {}
        head = self.root
        if head.next and head.next.next:
            slow = head.next
            fast = head.next.next
        else:
            return False

        while fast.next and fast.next.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


    def has_loop_hash(self):
        """
        Create a hashmap that stores each node that's been visited.  Key/value pair is the node, and an integer of index
        Iterate through the list one at a time with a while loop looking at the .next of the node.  If not .next, return None.
        Otherwise, once a match is found, return the value of the KV pair.
        Otherwise, move to the next node and increment idx
        """
        curr, idx = self.root, 0
        if not curr:
            return None
        seen = {curr: idx}
        while curr.next:
            curr = curr.next
            idx += 1
            if curr in seen:
                return seen[curr]
            seen[curr] = idx
        return None

    def has_loop_pointers(self):
        head = self.root
        if not head:
            return None
        elif not head.next and head.next.next:
            return None
        else:
            slow = head.next
            fast = head.next.next
            while fast.next and fast.next.next:
                if slow == fast:
                    slow = head
                    while slow != fast:
                        slow = slow.next
                        fast = fast.next
                    return slow
                slow = slow.next
                fast = fast.next.next
            return None


"""
Cases:
1. empty list
2. list w one num
3. list w no loop
4. list w a loop

"""


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
LL1 = LinkedList()
# LL1.populate(list_1)
LL1.list_to_looped_SLL(list_1, 5)
print(LL1.has_loop_hash())
#print(LL1.has_loop())





