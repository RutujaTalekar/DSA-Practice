class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Twisted version of Kadane's algorithm

        '''
        instead of tracking the max sum in circular array, 
        we can get the max sum and min sum
        [1, -2, 3, -2]
        So our max sum as per Kadane's would be => 3
        And min sum as per Kadane's would be => -2
        So what we can do is subtract min from total to get max
        => 0 - 3 = -3 
        compare this is max, and return whichever is higher.

        [5,-3,5]
        max = 5
        min = -3
        total = 7
        glob max = max(7 - (-3) => 10 or 5) => 10

        [-3,-2,-3]
        max = -2
        min = -8
        toatl = -8
        glob max = max(-8-(-8)=> 0 ,-2 ) add a condition, if total - min is 0 then return max

        '''
        
        max_sum = - float('inf')
        min_sum = float('inf')
        cur_max_sum = 0
        cur_min_sum = 0
        total = 0

        for num in nums:
            cur_max_sum = max(cur_max_sum + num, num)
            cur_min_sum = min(cur_min_sum + num, num)
            min_sum = min(cur_min_sum, min_sum)
            max_sum = max(cur_max_sum, max_sum)
            total += num
        
        return max(total - min_sum, max_sum) if (total-min_sum) != 0 else max_sum



