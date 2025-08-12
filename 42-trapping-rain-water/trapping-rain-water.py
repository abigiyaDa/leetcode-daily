class Solution:
    def trap(self, height: List[int]) -> int:
        # time o(n) and space 0(1)
        if not height: return 0
        n=len(height)
        l,r =  0 , n-1
        leftMax, rightMax = height[l],height[r]
        res = 0

        while l<r:
            if leftMax < rightMax :
                if (leftMax - height[l]) > 0:
                    res += leftMax - height[l]
                l+=1
                leftMax = max(leftMax, height[l])
                
            else:
                if (rightMax - height[r]) > 0 :
                    res+=rightMax - height[r]
                r-=1
                rightMax = max(rightMax,height[r])
                
        return res 


        # # time = o(2n) = o(n), space = o(n)
        # n=len(height)

        # max_right = [0]*n
        # max_right[n-1] = 0
        # for i in range(n-2,-1,-1):
        #     max_right[i] = max(height[i+1],max_right[i+1])
        # max_left = 0
        # res = 0
        # for i in range(n):
        #     m = min(max_right[i],max_left)
        #     x = m-height[i]
        #     if x > 0:
        #         res+=x
        #     max_left = max(height[i],max_left)
        # return res


        
