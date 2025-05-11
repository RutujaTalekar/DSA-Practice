class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        We can solve this problem by using the same 3 sum solution with another nested loop
        But since we want to provide a general solution for k sum, lets try to use recursion to solve this
        time - O(n3)
        '''

        res = []
        quad = []
        nums.sort()

        def ksum(k, start, target):
            if k!=2:
                # if k = 2, we will directly do 2 sum logic, if not use recursion instead of nested loops
                for i in range(start, len(nums)-k+1):
                    # deduplication logic
                    if i > start and nums[i] == nums[i-1]:
                        continue

                    quad.append(nums[i])
                    ksum(k-1, i+1, target-nums[i])
                    quad.pop()
            else:
                # now if k == 2, i.e. base case 
                l, r = start, len(nums)-1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l+=1
                    elif nums[l] + nums[r] > target:
                        r-=1
                    else:
                        # We already have first 2 values in quad, add that along with l and r to res
                        res.append(quad + [nums[l], nums[r]])
                        l += 1  # random, you can descrement r instead as well, do something to avoid infinite loop
                        while l < r and nums[l] == nums[l-1]:   # deduplication logic
                            l += 1 

            return
        
        ksum(4, 0, target)  # passing 4, since its 4 sum problem
        return res