class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # mem = [1]*(n+1)

        # if n <= 3:
        #     return n
        # for i in range(n, -1, -1):
        #     if i in (n, n-1):
        #         continue
        #     mem[i] = mem[i+1] + mem[i+2]

        # return mem[0]      

        # try using less space

        # represents the possible values of climbing the stairs from 2 consecutive steps
        step_1, step_2 = 1,1
        ans = 0
        if n <= 3:
            return n
        for i in range(n-2, -1, -1):
            ans = step_1 + step_2
            step_1 = step_2
            step_2 = ans
        return ans

