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
        if head is None:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next
        
        return True

        
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


        

