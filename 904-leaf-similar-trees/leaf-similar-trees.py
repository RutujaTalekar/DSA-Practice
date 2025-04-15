# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf = []
        
        def isLeaf(node):
            return node and not node.left and not node.right
            
        
        def DFS(node):
            if not node:
                return
            if isLeaf(node):
                leaf.append(node.val)
                return
            DFS(node.left)
            DFS(node.right)
            return
        
        
        DFS(root1)
        leaves1 = leaf[:]
        leaf.clear()
        DFS(root2)
        leaves2 = leaf[:]
        print(leaves1, leaves2)
        return leaves1== leaves2

            
