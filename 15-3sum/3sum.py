class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # N square using hash set
        '''
        result = set()
        nums.sort()

        for i in range(len(nums)):
            seen = set()
            target = -nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Optional: skip duplicate 'i' values
            for j in range(i+1, len(nums)):
                alternate = target - nums[j]
                if alternate in seen:
                    triplets = tuple(sorted([nums[i], nums[j], alternate]))
                    result.add(triplets)
                seen.add(nums[j])
        return list(result)
        '''
        


        # O(n square) | sorting + two sum 
        # result = []
        # nums.sort()



        # for i in range(len(nums)-2):
        #     left, right = i + 1 , len(nums) - 1
        #     while left < right:
        #         target_sum = nums[i] + nums[left] + nums[right]

        #         if target_sum > 0:
        #             right -= 1
        #         if target_sum < 0:
        #             left += 1
        #         else:
        #             result.append([nums[i], nums[left], nums[right]])
        #             left += 1
        #             right -= 1
        #             while left < right and nums[left] == nums[left -1]:
        #                 left +=1
        
        # return result


                

        
        # N square using Hashmap
        
        lookup = {num:i for i, num in enumerate(nums)}
        result = set()

        for i in range(len(nums)):
            target = 0 - nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Optional: skip duplicate 'i' values
            # two sum logic
            for j in range(i+1, len(nums)):
                new_target = target - nums[j]
                if new_target in lookup and lookup[new_target] not in (i,j):
                    result.add(tuple(sorted([nums[i], nums[j], new_target])))
        
        return list(result)
        

