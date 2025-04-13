# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS Recursive with high low limits

        low = - math.inf 
        high = math.inf

        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, low, high)


        
        # Inorder traversal of BST is in ascending order
        '''
        inOrder = []
        def inOrderBST(node):
            if not node:
                return
            if node.left:
                inOrderBST(node.left)
            inOrder.append(node.val)
            if node.right:
                inOrderBST(node.right)
        
        
        if root:
            inOrderBST(root)
            prev = inOrder[0]
            for i in range(1, len(inOrder)):
                if inOrder[i] <= prev:
                    return False
                prev = inOrder[i]
            print(inOrder)
        return True
        '''