# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS Recursive with high low limits
        # Inorder traversal of BST is in ascending order
        
        low = - math.inf 
        high = math.inf

        def validate(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        if not root:
            return True
        else:
            return validate(root.left, low, root.val) and validate(root.right, root.val, high)

