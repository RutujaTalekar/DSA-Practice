class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Dynamic programming problem - 
        Divide the main problem into subproblems
        The base case would be when length of nums is 1 -> 
        then the longest increasing subsequence will also be 1
        
        for i = 4
        dpt can be calculated by - LIS(4) = (1 + LIS(j), LIS(4)) for all j < i
        
        dpt = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dpt[i] = max(dpt[i], 1+ dpt[j])
        
        return max(dpt)
        '''

        sub = []

        for num in nums:
            # Manual binary search to find the insertion index
            left, right = 0, len(sub) - 1
            while left <= right:
                mid = (left + right) // 2
                if sub[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1

            # Now, left is the correct insertion position
            if left == len(sub):
                sub.append(num)
            else:
                sub[left] = num

        return len(sub)



        
        


