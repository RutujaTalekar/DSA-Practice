# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Instead of creating a new list and taking care of empty list edge case
        # its easier to create a dummy node, and then add the new list values to it

        dummy = ListNode(-1)
        cur = dummy
        # cur will be pointing to the latest added node of the output list

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        return dummy.next