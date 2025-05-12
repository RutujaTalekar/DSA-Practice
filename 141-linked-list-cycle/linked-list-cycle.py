# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Floyd's cycle detection - use slow and fast pointers to check cycle
        Time - O(n) and space - O(1)
        '''
        # if head is None:
        #     return False



        
        '''
        Using set to check visited nodes
        Time & Space - O(n)
        '''
        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        
        return False


        

