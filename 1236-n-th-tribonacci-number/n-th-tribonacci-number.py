class Solution:
    def tribonacci(self, n: int) -> int:
        # dynamic programming
        t0,t1,t2 = 0,1,1
        if n == 0:
            return t0
        if n < 3:
            return t1
        tn = 0
        i = 3
        while i <= n:
            tn = t0+t1+t2
            t0,t1,t2 = t1,t2,tn
            i+=1
        return tn
        



        # recursive solution - TLE
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        
            
        