# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use 2 ptrs to track current and next node, and reverse the direction of arrow
        '''

        prev, cur = None, head
        dummy = ListNode(-1)
        while cur:
            next_node = cur.next
            cur.next = prev
            dummy.next = cur
            prev, cur = cur, next_node
        return  dummy.next


            