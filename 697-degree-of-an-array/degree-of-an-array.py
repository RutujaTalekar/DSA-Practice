from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        left = {}
        right = {}

        for i, num in enumerate(nums):
            count[num] += 1
            if num not in left:
                left[num] = i
            right[num] = i

        degree = max(count.values())
        min_length = float('inf')

        for num in count:
            if count[num] == degree:
                length = right[num] - left[num] + 1
                min_length = min(min_length, length)

        return min_length


        