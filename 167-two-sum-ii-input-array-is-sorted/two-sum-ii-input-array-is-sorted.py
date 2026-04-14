class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first,last = 0, len(numbers)-1 
        while first < last:
            cur_sum = numbers[first]+ numbers[last]
            if cur_sum == target:
                return [first+1 , last+1]
            elif cur_sum < target:
                first +=1
            else :
                last -=1
            