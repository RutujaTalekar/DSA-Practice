# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # O(n^2) time but intuitive solution
        '''
        if not preorder or not inorder:
            return
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        '''

        # better time complexity o(n), dont use slicing or index() - this takes o(n)
        # What are we storing in map - values : index for inorder
        # the values will be same in preorder, so this will give us the index of inorder vals
        # when we are locating root vals in inorder
        # instead of sending sliced lists, use indexes from map

        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        self.pre_start = 0

        def build(in_start, in_end):
            if in_start > in_end:
                return
            
            root = TreeNode(preorder[self.pre_start])
            self.pre_start += 1
            mid = inorder_map[root.val]

            root.left = build(in_start, mid-1)
            root.right = build(mid+1, in_end)

            return root

        return build(0, len(inorder)-1)

        '''
        Note - inorder_map is read-only and defined in the outer scope, so Python allows access inside buildTreeHelper
                pre_start on the other hand gets updated, if you try to modify a variable from an outer scope, you must declare it nonlocal or make it an attribute like self.pre_idx
        '''

            


            
            


            
            




            
        
