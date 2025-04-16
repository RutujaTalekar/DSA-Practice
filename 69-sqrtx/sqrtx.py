class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x//2

        if x < 2:
            return x

        ans = 0
        target = x
        while left <= right:
            mid = (left + right) // 2
            square = mid**2

            if square == target:
                return mid

            if square > target:
                right = mid - 1
            
            elif square < target:
                left = mid + 1

                
        return right



        





