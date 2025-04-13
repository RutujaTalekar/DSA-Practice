# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # BFS Iterative
        if not root:
            return 0
        
        q = deque([root])
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return level




        # DFS Recursive
        # base case
        if not root:
            return 0


        # recursively check - 
        # height at root = 1 + max(left tree, right tree)
        # 1 is counting the root itself
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        