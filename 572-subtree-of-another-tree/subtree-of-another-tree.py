# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS Recursive
        # look for node subRoot match, once matched match other nodes like same tree problems
        def isSameTree( p, q):
            if not p and not q:
                return True
            if p and q:
                return (
                    p.val == q.val
                    and isSameTree(p.left, q.left)
                    and isSameTree(p.right, q.right)
                )
            return False

        # Interesting base case - if subRoot is null, then technically it can be a subtree of root. So return true
        if not subRoot:
            return True
        # if root is null and subRoot is not null then it cannot be a subTree
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
