class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit 
        
        # profit =0
        # buy = prices[0]
        # i=1
        # while(i<len(prices)):
        #     if buy > prices[i]:
        #         buy = prices[i]
        #     elif prices[i]-buy > 0:
        #         profit += (prices[i]-buy)
        #         buy = prices[i]
        #     i+=1
        # return profit

        