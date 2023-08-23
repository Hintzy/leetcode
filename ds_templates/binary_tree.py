class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return f'{self.root}'


