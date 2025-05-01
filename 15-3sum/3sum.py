class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorted array and two pointers
        # -4, -1, -1, 0, 1, 2
        result = set()
        nums.sort()
        seen = set()

        for i in range(len(nums)-2):
            if i in seen:
                continue
            lo, hi = i+1, len(nums)-1
            while (lo < hi):
                sum_target = nums[i] + nums[lo] + nums[hi]  # ideally equal to 0

                if sum_target > 0 :
                    hi -=1
                elif sum_target < 0:
                    lo +=1
                else:
                    result.add((nums[i], nums[lo], nums[hi]))
                    lo +=1
                    hi -=1

            seen.add(i)

        
        return list(result)






        # N square using hash set
        '''
        result = set()
        nums.sort()

        for i in range(len(nums)):
            seen = set()
            target = -nums[i]
            if i > 0 and nums[i] == nums[i - 1]:    # deduplication logic
                continue  # skips duplicate 'i' values, cause we have already found those triplets
            for j in range(i+1, len(nums)):
                alternate = target - nums[j]
                if alternate in seen:
                    triplets = tuple([nums[i], nums[j], alternate]) # we dont need to user sorted list as we are doing deduplication logic
                    result.add(triplets)
                seen.add(nums[j])
        return list(result)
        '''

        



        '''
        Note -  For 3 sum problem, hashmap storage doesnt work as opposed to 2 sum
                Because there can be duplicates in the list of numbers!!! 
                When you do this - lookup = {num:i for i, num in enumerate(nums)}
                it saves the index of last occurrence of that number, giving us false data
                Imp to check constraints!!
        '''
        

