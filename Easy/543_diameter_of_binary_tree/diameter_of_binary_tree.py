from ds_templates import binary_tree as bt
from typing import Optional


"""
Solution logic:
The previous problem completed before this was to determine the maximum depth of a binary tree.  This problem recursively
performed an inorder traversal of the tree, finding the maximum length path from the root by adding 1 to a numeric
counter each time another traversal occurred.

This solution will use a max_depth helper function that will find the max length of a leg of a tree (depth-1).
The max diameter of a tree at any given node will be the max length of the left leg added to the max length of the 
right leg.  The tree will be traversed inorder, calculating the maximum diameter of each node, and return the max of the
current node versus the overall max.  
"""

# L0
root1 = bt.TreeNode(4)

# L1
root1.left = bt.TreeNode(-7)
root1.right = bt.TreeNode(-3)

# L2
root1.right.left = bt.TreeNode(-9)
root1.right.right = bt.TreeNode(-3)

# L3
root1.right.left.left = bt.TreeNode(9)
root1.right.left.right = bt.TreeNode(-7)
root1.right.right.left = bt.TreeNode(-4)

# L4
root1.right.left.left.left = bt.TreeNode(6)
root1.right.left.right.left = bt.TreeNode(-6)
root1.right.left.right.right = bt.TreeNode(-6)

# L5
root1.right.left.left.left.left = bt.TreeNode(0)
root1.right.left.left.left.right = bt.TreeNode(6)
root1.right.left.right.left.left = bt.TreeNode(5)
root1.right.left.right.right.left = bt.TreeNode(9)

# L6
root1.right.left.left.left.left.right = bt.TreeNode(-1)
root1.right.left.left.left.right.left = bt.TreeNode(-4)
root1.right.left.right.right.left.left = bt.TreeNode(-2)


def diameterOfTree(root: Optional[bt.TreeNode]) -> int:

    def maxDepth(root):
        if root is None: return 0
        return 1 + max(maxDepth(root.left), maxDepth(root.right))

    def NodeDiam(root):
        if root is None: return 0
        return maxDepth(root.left) + maxDepth(root.right)

    if root is None: return 0
    max_d = max(0, NodeDiam(root))
    max_d = max(max_d, max(diameterOfTree(root.left), diameterOfTree(root.right)))

    return max_d



print(diameterOfTree(root1))

# def maxEdges(root):
#     if root is None: return 0
#     elif root.left:
#         left_max = 1 + max(maxEdges(root.left), maxEdges(root.right))
#     elif root.right:
#         right_max = 1 + max(maxEdges(root.left), maxEdges(root.right))
#     return max(left_max, right_max)