var maxProfit = function(prices) {
    var buy = prices[0]
    var profit = 0
    for(let i=0;i<prices.length;i++){
        y = prices[i]-buy
        if(buy > prices[i]){
            buy = prices[i]
        }
        else{
            profit = Math.max(profit,y)
        }
    }
    return profit
};