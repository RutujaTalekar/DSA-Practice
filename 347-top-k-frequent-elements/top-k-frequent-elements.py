import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        Solutiuon 3 is more space efficient than solution 2
        Since we maintain a heap of exactly size k during the iteration.
            Each operation is O(log k), and you do it for n items → O(n log k) overall.
            Memory stays at O(k) — you're never storing all n elements at once.   
        But for solution 2 - we store O(n)  
        '''
        # Solution 3, use heap - but efficient
        frequency = Counter(nums)
        min_heap = []

        for num, freq in frequency.items():
            heapq.heappush(min_heap, (freq,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]


        # Solution 2, use heap
        frequency = Counter(nums)
        heap = [(freq, num) for num, freq in frequency.items()]
        top_k = heapq.nlargest(k, heap)
        return [num for freq, num in top_k]

        


        # Solution 1, use Counter map and sorting by values
        frequency = Counter(nums)        
        sorted_keys_by_values = sorted(frequency.keys(), key = lambda x: - frequency[x])  # sorts the keys based on values in descending order
        return sorted_keys_by_values[:k]


        
        



        