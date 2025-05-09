class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        '''
        Variation of bounded Knapsack 0/1 problem
        Intuition explained in book notes, understand properly
        '''
        dpt = [0] * (budget + 1)  # +1 cause we will store values starting from 1
                                        # when budget = 0, max profit = 0, thats the base case
        
        for i in range(len(present)):
            cost = present[i]
            profit = future[i] - present[i]

            if profit < 0:
                continue
            
            for b in range(budget, cost-1, -1): # go backwards so we are not counting the same profit repeatedly
                dpt[b] = max(dpt[b], profit + dpt[b - cost])
        
        return dpt[budget]
        