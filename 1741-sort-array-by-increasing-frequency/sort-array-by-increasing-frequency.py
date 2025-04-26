class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        sorted_keys = sorted(freq.keys(), key = lambda x: (freq[x],-x))

        result = []
        for num in sorted_keys:
            result += [num]*freq[num]
        return result

        '''
        Bucket sort technique - 
        1. Build frequency map.
        2. Build buckets: buckets[i] = list of numbers with frequency i.
        3. For each bucket, sort numbers decreasingly.
        4. Collect numbers from low to high freq.


        Pq/heap technique - 
        1. Build frequency map.
        2. Build min-heap by (freq, -value).
        3. Pop from heap and build result.
        '''