class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        duplicates = {} # key - nums, val - indices
        for i, num in enumerate(nums):
            if num not in duplicates:
                duplicates[num] = [i]
            else:
                duplicates[num].append(i)
                diff = abs(duplicates[num][-1] - duplicates[num][-2])
                if diff <= k:
                    return True
        return False



        
        # print(duplicates)

        # for num, idx in duplicates:
        #     if len(idx) > 1:


        