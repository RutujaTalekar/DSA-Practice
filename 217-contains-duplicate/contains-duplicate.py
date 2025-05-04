class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using hashsets
        if len(nums) == len(set(nums)):
            return False
        return True


        # using counter map for frequency time - O(n)
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        for num, freq in frequency.items():
            if freq >= 2:
                return True
        
        return False




