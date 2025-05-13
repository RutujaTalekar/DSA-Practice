class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        '''
        Greedy approach 
        Time - O(n) Space - O(1)
        '''
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return True if goal == 0 else False

        


            



        