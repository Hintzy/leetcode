from ds_templates import binary_tree as bt
from ds_templates import test_series
from typing import Optional


def maxDepthBinTree(root: Optional[bt.TreeNode]) -> int:
    if root is None: return 0
    return 1 + max(maxDepthBinTree(root.left), maxDepthBinTree(root.right))


root1 = bt.TreeNode(3)
root1.left = bt.TreeNode(9)
root1.right = bt.TreeNode(20)
root1.right.left = bt.TreeNode(15)
root1.right.right = bt.TreeNode(7)

print(root1)
print(maxDepthBinTree(root1))
