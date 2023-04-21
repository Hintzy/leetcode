class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node ({self.data})'


# RECURSIVE METHOD
# rewt = Node(1)
# rewt.right = Node(2)
# rewt.right.left = Node(3)
#
# output = []
# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         output.append(root)
#         inorder_traversal(root.right)
#     return output
#
# print(inorder_traversal(rewt))

# ITERATIVE METHOD
"""

- While left or (not(left) AND right)
    if left:
        go left
    elif right:
        go right
     
- Propagate to the left as far as possible.  
    - Once none reached, see if right exists.
        - If right exists, go right. 
            - Propagate left as far as possible, if none reached, see if right exists.
Once none, see if there is a right
"""