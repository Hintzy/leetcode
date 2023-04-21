from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}, {self.next}'

def ord_to_linked_list(a: list[int]) -> Optional[ListNode]:
    if not a:
        return ListNode()

    head = ListNode(a[0])
    cur = head
    if len(a) > 1:
        for num in a[1:]:
            new_node = ListNode(num)
            cur.next = new_node
            cur = new_node
    return head


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode], res = None, carry = 0) -> Optional[ListNode]:

    if l1 is None and l2 is None:
        if carry == 0:
            return res
        else:
            new_node = ListNode(carry)
            res.next = new_node
            return res
    elif l1 is None:
        tot = l2.val + carry
    elif l2 is None:
        tot = l1.val + carry
    else:
        tot = l1.val + l2.val + carry

    carry, val = divmod(tot, 10)
    new_node = ListNode(val)

    if res is None:
        res = new_node
        tail = new_node
    else:
        res.next = new_node
        tail = new_node

    addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None, tail, carry)

    return res



list_1 = [4, 9, 8]
list_2 = [1, 2, 3]
lst_1 = ord_to_linked_list(list_1)
lst_2 = ord_to_linked_list(list_2)
print(addTwoNumbers(lst_1, lst_2))

# print(ord_to_linked_list(list_1))
# print(ord_to_linked_list(list_2))


"""
Initialize all and use a nested helper function

If both lists are none, return header of result list
If one list is none, next result node is equal to the current node of the remaining numbers list
Otherwise both lists still have values:
    For each result node, add the two nodes of the l1/l2 nodes:
        If value if greater than or equal to ten:
            Node value is equal to (sum % 10) and recurse with next list node vals with one +1
        If value less than ten current res node value is equal to sum
            Recurse with .next 
            

"""