class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        output = [0] * n
        leftBounds = [0] * n
        rightBounds = [0] * n
        rightMax, leftMax = 0, 0

        for i in range(n-1, -1, -1):
            if i == n-1:
                rightMax = height[n-1]
                rightBounds[i] = rightMax
            rightMax = max(rightMax, height[i])
            rightBounds[i] = rightMax
        
        for i in range(len(height)-1):
            if i == 0:
                leftBounds[i] = height[i]
                left_max = leftBounds[i]
            left_max = max(left_max, height[i])
            leftBounds[i] = left_max
        
        for i in range(1, n-1):
            h = min(leftBounds[i], rightBounds[i])
            water = h - height[i]
            if water > 0:
                output[i] = water

        return sum(output)