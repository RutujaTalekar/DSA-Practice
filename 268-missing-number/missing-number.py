class Solution:
    # def missingNumber(self, nums: List[int]) -> int:

    #     # O(n) time and o(n) space
    #     nums_set = set(nums)
    #     for i in range(len(nums)+1):
    #         if i not in nums_set:
    #             return i
    #     return -1
                
    #     # O(n) time and O(1) space
    #     res = len(nums)
    #     for i in range(len(nums)):
    #         res+=i-nums[i]
    #     return res
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        def search(num):
            left=0
            right=len(nums)-1
            while left<=right:
                middle=(left+right)//2
                if nums[middle]==num:
                    return True
                elif num>middle:
                    left=middle+1
                else:
                    right=middle-1
            return False
        for i in range(0,len(nums)+1):
            if not search(i):
                return i