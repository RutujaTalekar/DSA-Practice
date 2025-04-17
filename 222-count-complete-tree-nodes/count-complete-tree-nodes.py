# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        '''
        Property of perfect bin trees - (2^depth) - 1
        so recursively check extreme left and right heights from each node
        if left = right that means this subtree is perfect bin tree and we can use the formula
        if it doesnt match then count the root (1) and check if its children follow above property
        1 + countNodes(left) + countNodes(right)
        '''
        
        # recursive way
        def getRightHeight(node):
            if not node:
                return 0
            return 1 + getRightHeight(node.right)
        
        # iterative way
        def getLeftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        # main logic
        if not root:
            return 0
        
        heightL = getLeftHeight(root)
        heightR = getRightHeight(root)
        if heightL == heightR:
            return 2**heightL - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)



        



        