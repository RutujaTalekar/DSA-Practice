class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        '''
        Greedy approach
        Start from end, and use a goal variable to store current goal
        In the beginning goal = len(nums) -1, as we traverse back we can move it if its reachable
        Time - O(n)
        [2,3,1,1,4]
        '''
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return True if goal == 0 else False






        '''
        Bottom up dynamic programming approach - Intuitive but slow 
        Time - O(n square)
        Space - O(n)
        '''
        n = len(nums)
        dp = [False] * n
        dp[-1] = True  # We can always reach the end from the last index

        for i in range(n - 2, -1, -1):
            furthestJump = min(i + nums[i], n - 1)
            for j in range(i + 1, furthestJump + 1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]


            



        