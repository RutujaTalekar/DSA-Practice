import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Solution 2, use heap
        # get frequencies
        frequency = Counter(nums)
        # make list of tuples
        heap = [(freq, num) for num, freq in frequency.items()]
        heap = heapq.nlargest(k, heap)
        return [y for x,y in heap]

        


        # Solution 1, use Counter map and sorting by values
        frequency = Counter(nums)
        sorted_keys_by_values = sorted(frequency, key = lambda x: - frequency[x])  # sorts the keys based on values in descending order
        return sorted_keys_by_values[:k]


        
        



        