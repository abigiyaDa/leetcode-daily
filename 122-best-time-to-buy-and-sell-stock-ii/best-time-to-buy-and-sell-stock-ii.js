var maxProfit = function(prices) {
    var profit =0;
    var buy = prices[0];
    for(let i = 1; i < prices.length ;i++){
        if (buy > prices[i]){
            buy = prices[i];
        }
        else if ((prices[i]-buy) >0){
            profit += (prices[i]-buy);
            buy = prices[i];
        }
    }   
    return profit 
};