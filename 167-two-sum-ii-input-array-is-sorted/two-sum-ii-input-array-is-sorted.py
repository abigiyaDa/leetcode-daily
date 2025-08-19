class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # time o(n) space o(1)
        left = 0
        right = len(numbers)-1
        current_sum = 0
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target :
                return [left+1,right+1] # add one b/c its 1-indexed
            elif current_sum < target:
                left+=1
            else:
                right -= 1