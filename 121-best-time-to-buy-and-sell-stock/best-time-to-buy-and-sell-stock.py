class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = prices[0]
        # sell = 0
        # profit = 0
        # for i in range(1,len(prices)):
        #     sell = prices[i]
        #     y = sell - buy
        #     if buy > sell:
        #         buy = sell
        #     else:
        #         profit = max(profit,y)    
        # return profit  

        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            y = prices[i]-buy
            if buy > prices[i]:
                buy = prices[i]
            else:
                profit = max(profit,y)
        return profit
