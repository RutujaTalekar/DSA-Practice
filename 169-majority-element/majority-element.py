class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums_map = Counter(nums)

        for num, count in nums_map.items():
            if count > len(nums)/2:
                return num
            

        
        