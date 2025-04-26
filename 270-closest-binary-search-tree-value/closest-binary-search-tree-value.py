# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        # recursive solution with Binary Search 
        '''
        def search(node):
            if not node:
                return math.inf
            if node.val == target:
                return node.val
            if node.val < target:
                next_val = search(node.right)
            else:
                next_val = search(node.left)
            
            # based on dist pick the closest value
            if abs(next_val - target) < abs(node.val - target):
                return next_val
            elif abs(next_val - target) > abs(node.val - target):
                return node.val
            else:
                return min(next_val, node.val)

        return search(root)
        '''

        closest = root.val

        while root:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            elif abs(root.val - target) == abs(closest - target):
                closest = min(root.val, closest)
            root = root.left if target < root.val else root.right

        return closest

        # iterative approach
        closest = root.val
        while root:
            if root == target:
                return root.val
            closest = root.val if abs(root.val - target) < closest else closest
            root = root.left if root.val > target else root.right
        
        return closest 



        