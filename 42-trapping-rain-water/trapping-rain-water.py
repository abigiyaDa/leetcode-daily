class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
            
        max_right = [0]*n
        max_right[n-1] = 0
        for i in range(n-2,-1,-1):
            max_right[i] = max(height[i+1],max_right[i+1])
        max_left = 0
        res = 0
        for i in range(n):
            m = min(max_right[i],max_left)
            x = m-height[i]
            if x > 0:
                res+=x
            max_left = max(height[i],max_left)
        return res


        
