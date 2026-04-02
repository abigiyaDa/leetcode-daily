class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ones = sum(nums)
        zero = 0
        max_score = -1
        res = []
        for i in range(n+1):
            score = ones + zero
            if score > max_score:
                max_score = score
                res = [i]
            elif score == max_score:
                res.append(i)
            if i < n:
                zero += (1-nums[i])
                ones -= nums[i]
        return res


            


