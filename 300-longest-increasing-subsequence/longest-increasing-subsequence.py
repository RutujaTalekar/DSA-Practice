class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Dynamic programming problem - 
        Divide the main problem into subproblems
        The base case would be when length of nums is 1 -> 
        then the longest increasing subsequence will also be 1
        
        dpt can be calculated by - LIS(4) = (1 + LIS(i), LIS(4)) for all i < 4
        '''

        dpt = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dpt[i] = max(dpt[i], 1+ dpt[j])
        
        return max(dpt)

        
        


