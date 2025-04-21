"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        '''
        use cur_node and left_child pointers to traverse through the tree with BFS
        when at cur_node/ root you can connect its children
        ex - when at root - 1, connect left child -> 2 to right child -> 3
        for the next level, you can use cur_node.next i.e. 2's next ptr is already
        pointing to 3, so you can connect right child of 2 to left child of 3.
        End the process when cur_node or left_child becomes null
        '''
        # Note - if left child is present then by the property of perfect bin tree,
        # right child is also present.. thats why we can move ahead and connect them
        cur_node, left_child = root, root.left if root else None

        # start BFS
        while cur_node and left_child:
            cur_node.left.next = cur_node.right
            if cur_node.next:
                cur_node.right.next = cur_node.next.left
            
            cur_node = cur_node.next
            if not cur_node:
                cur_node = left_child
                left_child = cur_node.left

        return root
            





        