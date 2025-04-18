class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Using two pointer aproach on the sorted array
        # increase the pointer from either right or left depending on sum > target
        left, right = 0, len(numbers)-1

        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left+1, right+1]
            if res > target:
                right -=1
            if res < target:
                left += 1
        
        return []
        