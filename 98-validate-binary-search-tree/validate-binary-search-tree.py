# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inOrder = []
        # Inorder traversal of BST is in ascending order
        def inOrderBST(node):
            if not node:
                return
            if node.left:
                inOrderBST(node.left)
            inOrder.append(node.val)
            # if len(inOrder) > 1 and inOrder[-1] < inOrder[-2]:
            #     return False
            if node.right:
                inOrderBST(node.right)
            




            # if node.left and node.val < inOrderBST(node.left):
            #     return False
            # if node.right and node.val > inOrderBST(node.right):
            #     return False
        
        
        if root:
            inOrderBST(root)
            prev = inOrder[0]
            for i in range(1, len(inOrder)):
                if inOrder[i] <= prev:
                    return False
                prev = inOrder[i]
            print(inOrder)
        return True
                





        # DFS Recursive with high low limits
        '''
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
        '''
