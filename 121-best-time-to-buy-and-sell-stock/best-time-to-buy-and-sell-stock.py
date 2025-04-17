class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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




