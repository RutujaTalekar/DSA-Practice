# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        if root:
            q = deque([root])
            while q:
                node = q.popleft()
                node.left, node.right = node.right, node.left

                #add the children to the queue
                if (node.left):
                    q.append(node.left)
                if (node.right):
                    q.append(node.right)
        
        return root
        
        
        
        # # shorter clener DFS recursive solution
        # if root:
	    #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
	    
        # return root

        '''
        if not root:
            return None
        
        node = root.left
        root.left = root.right
        root.right = node

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        '''
        