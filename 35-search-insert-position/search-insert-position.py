class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
                
            else:
                left = mid + 1
        
        return left

        nums = [1, 3, 5, 6, 9, 15, 23]
        target = 10
        

        