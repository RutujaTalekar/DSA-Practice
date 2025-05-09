from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)   # to store frequency map of each num
        left = {}               # to store the first seen index of each num
        right = {}              # to store the last seen index of each num

        degree = max(count.values())
        result = math.inf

        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i

        for i in range(len(nums)):
            if count[nums[i]] == degree:
                length = right[nums[i]] - left[nums[i]] + 1
                result = min(length, result)
        
        return result
                        





        