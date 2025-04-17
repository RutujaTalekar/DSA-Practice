class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        
        #Accpted, finds daily profits and uses maximum subarray(dp) to find max profit
        '''
        profits = []
        if len(prices) <= 1:
            return 0

        for i in range(1,len(prices)):
            profit = prices[i] - prices[i-1]
            profits.append(profit)

        maxi = 0
        dp = [0]*len(profits)
        dp[0] = profits[0]

        for i in range(1,len(profits)):
            dp[i] = max(profits[i], dp[i-1]+profits[i])

        if max(dp) < 0:
            return 0
        return max(dp)
        '''

        


        best = 0
        buy = prices[0]

        for sell in prices[1:]:
            profit = sell-buy

            if profit < 0:
                buy = sell
            elif profit>0 and profit>best:
                best = profit
            else:
                pass
                
        return best




        '''
        Brute force - Time complexity O(n), space complexity - O(1)

        maxProfit = 0

        if not prices:
            return 0
        buy, sell, profit = prices[0], prices[0], 0

        for i in range(len(prices)):
            if prices[i] < buy and i != len(prices)-1:
                buy = prices[i]
                sell = buy
            
            if prices[i] > sell :
                sell = prices[i]
            
            profit = sell - buy
            maxProfit = max(profit, maxProfit)
        
        return maxProfit
        '''




