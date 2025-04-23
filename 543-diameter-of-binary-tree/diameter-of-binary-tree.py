# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Note - diameter doesnt necessarily have to be pass through the root.
        Calculating left extreme height plus right extreme height wont give us the diameter
        use dfs to rcursively calculate max height out of left and right branches
        use a global variable to store the max diameter based on the heights
        '''

        self.diameter = 0

        # this will return height
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left+right)

            return max(left,right) + 1  # +1 as that will count the root node edge
        

        dfs(root)
        return self.diameter
            

        