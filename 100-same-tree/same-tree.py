# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # cleaned up DFS
        
        if not p and not q:
            return True
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return False
        
        # bfs iterative
        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        qu = deque([(p, q)])

        while qu:
            pNode, qNode = qu.popleft()

            if not pNode and not qNode:
                continue
            if not pNode or not qNode:
                return False
            if pNode.val != qNode.val:
                return False

            # Always enqueue both children, even if None
            qu.append((pNode.left, qNode.left))
            qu.append((pNode.right, qNode.right))

        return True

        '''

        

        