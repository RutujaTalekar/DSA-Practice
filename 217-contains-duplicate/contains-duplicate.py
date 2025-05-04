class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using hashsets
        # if len(nums) == len(set(nums)):
        #     return False
        # return True


        # using counter map for frequency time - O(n)
        frequency = {}
        for num in nums:
            if num in frequency:
                return True
            else:
                frequency[num] = 1
        
        return False




