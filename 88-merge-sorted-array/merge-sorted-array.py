class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """

        '''
        compare each element one by one of nums1 and nums2, untill one of them is traversed completely
        Add the rest of the items wherever left nums1/nums2
        Above soln works but it needs extra temp list to store sorted list.

        To do it in O(1) space and to follow the conditions given, we can try adding from the end.
        We are already left the amount of space we would need.
        so compare last element of nums1 and nums2 with each other, and add the largest at end, do it for all elements.
        '''

        # we need pointers to get last element of nums1, nums2 and position of insert from end of nums1
        i, j = m-1, n-1
        insert_at = m+n-1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[insert_at] = nums1[i]
                i -=1
            else:
                nums1[insert_at] = nums2[j]
                j -=1
            insert_at -=1
        
        # in case insert_at is not reached 0, and nums2 has elements left, then we can directly add them
        while j >= 0:
            nums1[insert_at] = nums2[j]
            j -= 1
            insert_at -=1

        # in case insert_at is not reached 0, and nums2 has elements left, then we can directly add them
        while i >= 0:
            nums1[insert_at] = nums1[i]
            i -= 1
            insert_at -=1
        

        # in case nums1 doesnt have any elements of its own
        if m+n == n:
            nums1[:] = nums2[:]


    





        

                
            

            

                
            

        




            

        