class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        # edge case 
        freq = Counter(nums)
        if len(freq) == 1:
            return 0
        
        # helper function
        def costCalculator(ele):
            total = 0
            for i, num in enumerate(nums):
                diff = abs(num - ele) * cost[i]
                total += diff
            return total
        

        # We can use binary search to find optimal cost. 
        '''
        Our seach space will be between min(nums) and max(nums)
        mid is a middle number, for example one, left = 1, right = 5 and mid = 3, so find cost(3)
        We also calculate the cost of 2 adjacent nums to mid, i.e. cost(2) and cost(4)

        Now we want to check if the cost(mid) > cost(mid+1), if it is then we know that 
        optimal element to pick to change all others reside in right half so -> left = mid + 1
        otherwise right = mid

        left will always give the min cost

        Let n be the length of the input array nums and k be the difference between the maximum and minimum value of nums
        So Time - O(log k * n) [helper function is o(n), and binary search is O(log k)]
        space - O(1)
        '''

        left = min(nums)
        right = max(nums)
        min_cost = 0
        while left < right:
            mid = (left+right)//2
            mid_cost = costCalculator(mid)
            mid_next_cost = costCalculator(mid+1)

            if mid_cost > mid_next_cost:
                # this means that optimal solution is on right side of the space. since we are looking for minimum - we return left's cost
                left = mid + 1
            else:
                right = mid
            
            min_cost = min(mid_cost, mid_next_cost)

        return min_cost


        # brute force O(n2)
        minCost = math.inf
        for num in nums:
            minCost = min (minCost, costCalculator(num))
        
        return minCost


        '''
        In some binary search problems, we are not searching for an exact values (like target == mid),
        Rather we are relying on either left or right index to get the optimal solution
        
        Because we are not explicitly checking mid == target, we must not skip over mid by doing right = mid - 1.
        This is why we are not adjusting bounds to our usual [left = mid + 1 and right = mid - 1 ]
        instead we are doing right = mid, so we dont skip over the mid value as we are not explicitly checking for it

        Also, because of this, we cannot stop at left <= right, this will run infinitely if left = right = mid
        so we stop at left < right: 

        In this case, the comparison is not equality-based, but slope-based — like:
            cost(mid) > cost(mid + 1) → move right (minimum lies to the right)
            cost(mid) <= cost(mid + 1) → move left (minimum lies to the left, or at mid)
        '''
