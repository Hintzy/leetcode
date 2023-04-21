from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode({self.val})'

    def display_keys(self, node, space='\t', level=0):  # written by Jovian
        # print(node.key if node else None, level)

        # If the node is empty
        if node is None:
            print(space * level + 'Ø')
            return

        # If the node is a leaf
        if node.left is None and node.right is None:
            print(space * level + str(node.val))
            return

        # If the node has children
        self.display_keys(node.right, space, level + 1)
        print(space * level + str(node.val))
        self.display_keys(node.left, space, level + 1)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return f'Tree({self.root})'


data_list = [x for x in range(32)]
def list_2_bst(lst: list[int], lo: int = 0, hi: int = 0, depth: int = 0) -> Optional[TreeNode]:
    if depth == 0:
        lo = 0
        hi = len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = lst[mid]
        root = TreeNode(val)
        root.left = list_2_bst(data_list, lo, mid-1, depth + 1)
        root.right = list_2_bst(data_list, mid+1, hi, depth + 1)
        return root

root = list_2_bst(data_list)
root.display_keys(root)
