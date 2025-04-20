class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # O(n) time and o(n) space
        nums_set = set(nums)
        for i in range(len(nums)+1):
            if i not in nums_set:
                return i
        return -1
                
        # O(n) time and O(1) space
        res = len(nums)
        for i in range(len(nums)):
            res+=i-nums[i]
        return res