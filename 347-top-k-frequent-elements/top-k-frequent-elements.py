class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1, use Counter map
        frequency = Counter(nums)
        res = sorted(frequency, key = lambda x: -frequency[x])
        return res[:k]



        