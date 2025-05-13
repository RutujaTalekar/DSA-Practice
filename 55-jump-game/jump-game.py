class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        Bottom up dynamic programming approach - Intuitive but time O(n square)
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


            



        