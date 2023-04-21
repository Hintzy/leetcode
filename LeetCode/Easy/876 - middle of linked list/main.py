# Definition for singly-linked list.
hed = []
hd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


from math import ceil

class ListNode:
    def __init__(self, val=0, next=None, node_index=0):
        self.val = val
        self.next = next
        self.node_index = node_index

    def __str__(self):
        return f'[{self.val}, {self.next}]'


def create_linked_list(head):
    if not head:
        return None

    head_node = ListNode(head[0], node_index=0)
    current_node = head_node
    # count = 1
    for i, num in enumerate(head[1:]):
        new_node = ListNode(num, node_index=(i+1))
        current_node.next = new_node
        # print(f'Object #{count} - Val {current_node.val}  Next Node Val - {new_node.val}')
        # count += 1
        current_node = new_node
    # print(f'Object #{count} - Val {current_node.val}  Next Val - {current_node.next}')
    return head_node


def linked_list_len(head):
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length


def find_middle(head, length):
    if length % 2 == 0:
        node_index = ceil(length / 2)
    else:
        node_index = length // 2
    while head.node_index != node_index:
        head = head.next
    return head


linked_list = create_linked_list(hd)
length = linked_list_len(linked_list)
print(length)
print(find_middle(linked_list, length))
# print(linked_list_len(linked_list))
