class Solution:
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n < 2:
            return n
        
        def compare(a, b):
            if a > b: return 1
            if a < b: return -1
            if a == b: return 0
        
        left = 0
        max_len = 1
        prev_cmp = 0
        
        for right in range(1, n):
            curr_cmp = compare(arr[right-1], arr[right])
            
            if curr_cmp == 0:
                left = right
            elif prev_cmp * curr_cmp != -1:
                left = right - 1
            
            max_len = max(max_len, right - left + 1)
            prev_cmp = curr_cmp
        
        return max_len