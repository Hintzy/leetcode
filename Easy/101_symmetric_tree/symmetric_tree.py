from typing import Optional


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode({self.val})'


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return f'BinaryTree({self.root.left}, {self.root}, {self.root.right})'


    def display_keys(self, node, space='\t', level: int = 0):
        # Condition to catch null left nodes
        if node is None:
            return (f'{space}' * level) + '∅\n'

        # Condition to catch leaf nodes
        if node.left is None and node.right is None:
            return (f'{space}' * level) + f'{node.val}\n'

        # Inorder traversal starting with the right subtree instead of the typical left (for viewability of output)
        # printing the node values as it traverses the tree
        return self.display_keys(node.right, level=level+1) + (f'{space}'*level)+f'{node.val}\n' + self.display_keys(node.left, level=level+1)

def is_mirror_1(root):
    """
    Takes the node of a binary tree and tells if the binary subtrees below that node are symettric to one another
    from that node.  Intended to be used on the root node of a binary tree.
    """
    if root is None:
        return True

    def inorder_left(root: TreeNode):
        """An inorder traversal starting with the left subnode"""
        if root is None:
            return '∅'
        return [inorder_left(root.left)] + [root.val] + [inorder_left(root.right)]

    def inorder_right(root: TreeNode):
        """An inorder traversal starting with the left subnode"""
        if root is None:
            return '∅'
        return [inorder_right(root.right)] + [root.val] + [inorder_right(root.left)]

    return inorder_left(root.left) == inorder_right(root.right)
        # def preorder_right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
david = BinaryTree(root)


print(david.display_keys(root))

print(is_mirror_1(root))

