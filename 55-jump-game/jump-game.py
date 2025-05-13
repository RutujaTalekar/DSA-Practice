class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Greedy approach - instead of starting from 0 idx and reaching last idx as goal
        lets start from end and reach 0 as a goal

        At every poisition from the second last, check if you can reach the last idx
        If you can - then your goal is now changed to reaching that particular idx

        Initialize goal ptr to len of nums
        Traverse reverse
        If we can reach the goal from cur idx we can shift the goal cur idx
        '''
        goal = len(nums)-1

        for idx in range(len(nums)-1, -1, -1):
            if idx + nums[idx] >= goal:
                goal = idx
        
        return True if goal==0 else False
        
        '''
        You can use dynamic programming or greedy approach
        With dynamic programming and memoization, you need O(n square) time and O(n) space
        With greedy, you need O(n) time and O(1) space
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





        