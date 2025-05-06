# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False

        qu = deque()
        qu.append((p,q))

        while qu:
            for _ in range(len(qu)):
                p, q = qu.popleft()
                if not p:
                    if q:
                        return False
                    continue
                        
                if not q:
                    if p:
                        return False
                    continue

                if p.val == q.val:
                    qu.append((p.left,q.left))
                    qu.append((p.right,q.right))
                else:
                    return False

        return True