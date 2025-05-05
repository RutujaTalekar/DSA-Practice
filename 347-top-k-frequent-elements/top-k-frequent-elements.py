class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1, use Counter map
        frequency = Counter(nums)
        res = sorted(frequency.keys(), key = lambda x: -frequency[x])  # sorts the keys based on values in descending order
        return res[:k]



        