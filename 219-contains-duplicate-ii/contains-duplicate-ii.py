class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        '''
        Maintain a hashmap with (num -> [indices]) 
        As you append the index of repeated num, check if the abs diff is less than k
        '''
        duplicates = {}
        for i, num in enumerate(nums):
            if num in duplicates and i - duplicates[num] <= k:
                return True
            duplicates[num] = i
        return False



        duplicates = {}
        for i, num in enumerate(nums):
            if num not in duplicates:
                duplicates[num] = [i]
            else:
                duplicates[num].append(i)
                diff = abs(duplicates[num][-1] - duplicates[num][-2])
                if diff <= k:
                    return True
        return False



        