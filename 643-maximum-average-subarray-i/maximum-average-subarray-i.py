class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)-1
        cur_sum = sum(nums[:k])
        max_avg = cur_sum/k
        start = 0
        end = k-1
        while end < n:
            cur_sum -= nums[start]
            start+=1
            end+=1
            cur_sum += nums[end]
            if (cur_sum/k) > max_avg:
                max_avg = (cur_sum/k)
        return max_avg
        