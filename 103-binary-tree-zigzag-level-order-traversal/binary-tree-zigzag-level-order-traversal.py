# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []
        level = 0

        while q:
            level_nodes = []
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level % 2 == 0:
                res.append(level_nodes[::-1])
            else:
                res.append(level_nodes)
        
        return res
