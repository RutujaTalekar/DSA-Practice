# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """

        # better time complexity o(n), dont use slicing or index() - this takes o(n)
        # What are we storing in map - values : index for inorder
        # instead of sending sliced inorder, use indexes from map
        # postorder is just for locating root, which will be last value of list.

        if not inorder or not postorder:
            return None

        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def build(in_start, in_end):
            if in_start > in_end:
                return None

            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)
            self.post_idx -= 1

            mid = inorder_index[root_val]

            root.right = build(mid+1, in_end)
            root.left = build(in_start, mid-1)
            
            return root

        return build(0, len(inorder) - 1)

    

        # # O(N SQUARE) since we are using index function
        # if not inorder or not postorder:
        #     return None
        
        # root = TreeNode(postorder[-1])
        # mid = inorder.index(postorder[-1])

        # root.left = self.buildTree(inorder[:mid], postorder[:mid])
        # root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])

        # return root



        