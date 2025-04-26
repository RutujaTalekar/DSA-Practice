class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        sorted_keys = sorted(freq.keys(), key = lambda x: (freq[x],-x))

        result = []
        for num in sorted_keys:
            result += [num]*freq[num]
        return result