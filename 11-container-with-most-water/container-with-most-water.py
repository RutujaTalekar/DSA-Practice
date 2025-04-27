class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        
        # Efficient two pointer approach O(n)
        # place left and right pointers on extreme ends and calculate are to maximize
        # calculate area of rectangle - length * breadth
        # length is width right - left
        # breadth is height of min side

        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            area = h * (right - left)
            result = max(result, area)
            # dont forget to increment pointers, increment whatever was used
            if height[left]< height[right]:
                left += 1
            else:
                right -= 1
        return result

        # Brute force - Time limit exceeded O(n square)
        result = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = (j-i) * min(height[j],height[i])
                result = max(result, area)
        
        return result
            