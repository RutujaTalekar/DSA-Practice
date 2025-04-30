class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        # maintain monotonic stack - increasing order
        stack = []

        for i, num in enumerate(nums):
            
            while stack and num < stack[-1] and len(stack) + (len(nums) - i) > k:
                temp = len(stack) + (len(nums) - i)
                stack.pop()
            
            if len(stack) < k:
                stack.append(num)
        
        return stack

        '''
        Imp condition - 
        len(stack) + (n - i) > k 
        *** Can I safely pop the curr element from the stack and still be able to pick k elements later?
        
        len(stack) → number of elements you've already picked.
        n - i → number of elements remaining in nums, including the current one at index i.
        k → total number of elements you need to pick.
        '''


        return stack
        # Brute force O(nk) - Time limit exceeded
        seq = []
        temp = 0

        while k > 0:
            idx = temp
            mini = math.inf
            while idx <= len(nums) - k:
                if nums[idx] < mini:
                    mini = nums[idx]
                    temp = idx + 1
                idx += 1

            seq.append(mini)
            k -= 1
        
        return seq

            
        