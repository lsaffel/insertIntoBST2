# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if root is None:
            root = new_node
            return root

        if val < root.val:
            if root.left is None:
                root.left = new_node
            else:
                self.insertIntoBST(root.left, val)
        else:  # val > root.val
            if root.right is None:
                root.right = new_node
            else:
                self.insertIntoBST(root.right, val)

        return root
