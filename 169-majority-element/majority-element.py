class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # nums_map = Counter(nums)

        # for num, count in nums_map.items():
        #     if count > len(nums)/2:
        #         return num

        numMap = {}
        for num in nums:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
            
            if numMap[num] > len(nums)/2 :
                return num

            



        
        