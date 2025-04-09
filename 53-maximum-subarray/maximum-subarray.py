class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Brute force - O(n^2)
        # start with 2 loops, the inner loop will start from the index
        # of first loop, and traverse till end to find local max
        # continue this for the entire len of elements for first loop
        # return max sum

        # Kadane's algorithm - O(n)
        # start with one loop, traverse element
        # keep adding to the sum
        # if sum < next element or even 0 then discard sum, and reset as next element or 0

        local_sum = 0
        max_sum = nums[0] # or negative infinity

        for num in nums:
            local_sum += num
            max_sum = max(max_sum, local_sum)
            if local_sum < 0:
                local_sum = 0
        
        return max_sum

        