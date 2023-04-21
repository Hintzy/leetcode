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

    def convert_to_array(self):
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr

    def isPalindrome_v1(self) -> bool:
        """  Iterative appraoch:
        convert the linked list to a regular list, perform negative slicing on the list to reverse it and compare it to
        the value of itself this will be costly with regards to both space and time.  The function must traverse the
        linked list to create the array first
        """
        arr = self.convert_to_array()
        return arr == arr[::-1]


    def isPalindrome_v2(self, head):
        if head is None or head.next is None:
            return True

        # Find the middle of the list
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            print(head)
        print(f'2nd half: {slow}')


        # Reverse the second half of the list
        prev = None
        cur = slow
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        print(f'2nd reversed: {prev}')
        print(head)


        # Compare first half vs. second half
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

list_1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
LL1 = LinkedList()
LL1.populate(list_1)
print(f'full list: {LL1}')
print(LL1.isPalindrome_v2(LL1.head))