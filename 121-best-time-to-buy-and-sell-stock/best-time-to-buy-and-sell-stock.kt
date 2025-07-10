class Solution {
    fun maxProfit(prices: IntArray): Int {
        var buy = prices[0]
        var profit =0
        for (i in prices){
            if (i < buy) {
                buy = i
            }
            else{
                profit=maxOf(profit,i-buy)
            }
        }
        return profit
    }
}