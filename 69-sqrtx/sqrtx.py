class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x//2

        if x < 2:
            return x
        while left <= right:
            mid = (left + right) // 2
            square = mid**2
            if x >= square:
                left = mid + 1
            else:
                right = mid - 1
                
        
        return right



        





