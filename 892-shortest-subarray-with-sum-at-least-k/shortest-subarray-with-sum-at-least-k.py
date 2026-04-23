from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        dq = deque()
        res = float('inf')
        
        for j in range(n + 1):
            # Try to satisfy condition
            while dq and prefix[j] - prefix[dq[0]] >= k:
                res = min(res, j - dq.popleft())
            
            # Maintain increasing prefix
            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(j)
        
        return res if res != float('inf') else -1