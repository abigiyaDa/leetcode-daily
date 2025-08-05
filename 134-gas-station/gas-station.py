class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        last_gas = 0

        for i in range(len(gas)):
            last_gas += gas[i]-cost[i]
            if last_gas < 0:
                start =i+1
                last_gas = 0
        return start 

        