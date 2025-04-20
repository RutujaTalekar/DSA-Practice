# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        F F T T T T T T
        1 2 3 4 5 6 7 8

        F F F F F F T T
        1 2 3 4 5 6 7 8
        '''

        # left,right = 1, n
        # while(left<=right):
        #     mid = (left + right)//2

        #     if isBadVersion(mid) == True:
        #         if isBadVersion(mid-1) == False:
        #             return mid
        #         right = mid - 1
            
        #     if isBadVersion(mid) == False:
        #         left = mid + 1

        # return - 1


        l = 1
        r = n
        while l < r : 
            mid = (l+r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l =  mid + 1
        return l

            







        



        
        