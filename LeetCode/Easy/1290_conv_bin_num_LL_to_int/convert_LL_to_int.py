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

    def list_to_int_1(self):
        """Requires redefining a single-linked list to allow for curr.prev attributes"""
        head = self.root
        curr = head
        prev = curr
        while curr.next:
            curr = curr.next
            curr.prev = prev
            prev = prev.next

        pwr, tot = 0, 0
        while curr:
            tot += curr.val * (2 ** pwr)
            pwr += 1
            curr = curr.prev
        return tot

    def list_to_int_2(self):
        """
        Method copies values of single linked list into a list for handling that way.
        """
        bin_num, tot = [], 0
        head = self.root
        curr = head
        while curr:
            bin_num.append(curr.val)
            curr = curr.next
        for i, num in enumerate(bin_num[::-1]):
            tot += (num * (2 ** i))
        return tot


    def list_to_int_3(self, head):
        res = 0
        while head:
            res <<= 1
            res += head.val
            head = head.next

        return res


list_1 = [1, 0, 1, 1, 0, 1]
LL1 = LinkedList()
LL1.list_to_SLL(list_1)
print(LL1.list_to_int_3(LL1.root))



