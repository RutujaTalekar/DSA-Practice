class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x//2

        if x < 2:
            return x

        ans = 0

        while left <= right:
            mid = (left + right) // 2
            square = mid**2

            if x == square:
                return mid

            if x < square:
                right = mid - 1
        
            else:
                left = mid + 1
                ans = mid
                
        return ans



        





