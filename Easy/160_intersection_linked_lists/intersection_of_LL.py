from typing import Optional

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None



def get_intersection_node_1(head_a, head_b) -> Optional[ListNode]:
    hash_A = {}
    hash_B = {}
    curr_A = head_a
    curr_B = head_b
    while curr_A and curr_B:
        hash_A[curr_A] = curr_A.val
        hash_B[curr_B] = curr_B.val
        if curr_B in hash_A:
            return curr_B
        if curr_A in hash_B:
            return curr_A
        curr_A = curr_A.next
        curr_B = curr_B.next
    if curr_A:
        while curr_A:
            hash_A[curr_A] = curr_A.val
            if curr_A in hash_B:
                return curr_A
    elif curr_B:
        while curr_B:
            hash_B[curr_B] = curr_B.val
            if curr_B in hash_A:
                return curr_B
    return None


def get_intersection_node_2(head_a, head_b) -> Optional[ListNode]:
    curr_A = head_a
    curr_B = head_b
    while curr_A and curr_B:
        if curr_B is curr_A:
            return curr_B
        if curr_A is curr_B
            return curr_A
        curr_A = curr_A.next
        curr_B = curr_B.next
    if curr_A:
        while curr_A:
            if curr_A is curr_B:
                return curr_A
    elif curr_B:
        while curr_B:
            if curr_B is curr_A:
                return curr_B
    return None