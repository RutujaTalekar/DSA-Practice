class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        '''
        Can start from extreme ends cause logically that rectangle would have most width i.e. more water

        '''

        left, right = 0, len(height)-1
        area = - float('inf')
        while left< right:
            if height[left] < height[right]:
                l = height[left]
                b = right - left
                left += 1

            else:
                l = height[right]
                b = right - left
                right-=1

            
            area = max(area, l*b)
        
        return area
            



        