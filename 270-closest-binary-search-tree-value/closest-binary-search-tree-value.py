# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        # recursive solution with Binary Search
        def search(node):
            if not node:
                return math.inf
            if node.val == target:
                return node.val
            if node.val < target:
                next_val = search(node.right)
            else:
                next_val = search(node.left)
            
            # now pick the smallest value between the closest node 
            # among left or right children and the passed node value, and return that
            if abs(next_val - target) < abs(node.val - target):
                return next_val
            elif abs(next_val - target) > abs(node.val - target):
                return node.val
            else:
                return min(next_val, node.val)

        
        return search(root)



        