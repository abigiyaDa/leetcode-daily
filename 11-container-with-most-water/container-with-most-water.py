class Solution:
    def maxArea(self, height: List[int]) -> int:
        #2 pointer
        r=len(height)-1
        l=0
        max_area = 0
        while l<r:
            h=min( height[l] , height[r])
            w=r-l
            max_area = max(max_area,h*w)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return max_area

