class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dpt = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i]> nums[j]:
                    dpt[i] = max(dpt[j]+1, dpt[i])
    
        return max(dpt)



        '''
        Dynamic programming problem - EASIER APPROACH O(n square)
        Divide the main problem into subproblems
        The base case would be when length of nums is 1 -> 
        then the longest increasing subsequence will also be 1
        
        for i = 4
        dpt can be calculated by - LIS(4) = (1 + LIS(j), LIS(4)) for all j < i
        '''
        # dpt = [1]*len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(0, i):
        #         if nums[j] < nums[i]:
        #             dpt[i] = max(dpt[i], 1+ dpt[j])
        
        # return max(dpt)

        '''
        Binary Search solution, less intuitive but faster O(n logn)
        find max LIS length using binary search instead of maintaining local max
        '''
        sub = []

        for num in nums:
            # Manual binary search to find the insertion index in subsequence
            left, right = 0, len(sub) - 1
            while left <= right:
                mid = (left + right) // 2
                if sub[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1

            # Now, left is the correct insertion position
            if left == len(sub):    # left will either 0 or equal to the length of sub, that means -
                sub.append(num)     # cur num is  greater than the elements or sub is currently null
            else:
                sub[left] = num     # otherwise the num is smaller than the element at sub[left] so replace it

        return len(sub)



        
        


