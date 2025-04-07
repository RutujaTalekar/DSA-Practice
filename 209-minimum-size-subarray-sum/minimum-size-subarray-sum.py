class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        # Brute force - 
        # iterate over nums, keep adding each num to sum, start from i = 0
        # check after each addition if sum == target
        # if true save number of elements in a list and reset sum to 0
        # Continue again with i = 1
        # time complexity N square

        # Sliding window
        if len(nums) == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0
        
        if not nums:
            return 0


        local_sum = 0
        idx = 0
        prev = 0
        result = float('inf')
        while idx<len(nums):
            local_sum += nums[idx]
            while local_sum >= target:
                result = min(result, (idx+1)-prev)
                local_sum -= nums[prev]
                prev +=1
            idx += 1 
        return result if result != float('inf') else 0







        