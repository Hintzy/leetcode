from typing import Optional
from ds_templates import binary_tree as bt
from ds_templates import test_series as ts


"""
Logic:
The algorithm will perform an inorder traversal of the binary tree using recursion.  Up front, edge cases of a null root
node returns null. If the current node is not none, the left and right subnodes are swapped. The recursion occurs 
calling the function on root.left and root.right. Finally, root is returned.
"""



root1 = bt.TreeNode(2)
root1.left = bt.TreeNode(1)
root1.right = bt.TreeNode(3)
root1.left.left = bt.TreeNode(4)
root1.left.right = bt.TreeNode(5)
root1.right.left = bt.TreeNode(6)
root1.right.right = bt.TreeNode(7)

print(root1)


def invertBinaryTree(root: Optional[bt.TreeNode]):
    # if the tree is null, return None
    if not root: return None
    else:
        root.left, root.right = root.right, root.left

    #recursive function calls to perform inorder traversal
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)

    # finally, return the root of the tree
    return root

rversed = invertBinaryTree(root1)
print(rversed)