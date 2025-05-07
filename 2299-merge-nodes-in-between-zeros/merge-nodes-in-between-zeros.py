# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 
        sum_nodes = 0
        head = head.next    # take out the 0 at start of list

        while head:      
            if head.val == 0:
                node = ListNode(sum_nodes)
                curr.next = node
                curr = curr.next
                sum_nodes = 0
                

            sum_nodes += head.val
            head = head.next
        
        return dummy.next

            

                
