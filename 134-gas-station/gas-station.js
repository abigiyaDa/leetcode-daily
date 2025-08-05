var canCompleteCircuit = function(gas, cost) {
    if ((gas.reduce((a, b) => a + b, 0))<(cost.reduce((a, b) => a + b, 0))){
        return -1
    }
    var start =0
    var last_gas = 0
    for (let i =0 ; i<= gas.length ; i++){
        last_gas+= gas[i] - cost[i]
        if (last_gas < 0){
            start = i+1
            last_gas =0
        }
    }
    return start
    
};