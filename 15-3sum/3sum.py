class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # N square using hash set
        result = set()
        nums.sort()

        for i in range(len(nums)):
            seen = set()
            target = -nums[i]
            if i > 0 and nums[i] == nums[i - 1]:    # deduplication logic
                continue  # Optional: skip duplicate 'i' values
            for j in range(i+1, len(nums)):
                alternate = target - nums[j]
                if alternate in seen:
                    triplets = tuple([nums[i], nums[j], alternate]) # we dont need to user sorted list as we are doing deduplication logic
                    result.add(triplets)
                seen.add(nums[j])
        return list(result)

        # try using sorted array and two pointers



        '''
        Note -  For 3 sum problem, hashmap storage doesnt work as opposed to 2 sum
                Because there can be duplicates in the list of numbers!!! 
                When you do this - lookup = {num:i for i, num in enumerate(nums)}
                it saves the index of last occurrence of that number, giving us false data
                Imp to check constraints!!
        '''
        

