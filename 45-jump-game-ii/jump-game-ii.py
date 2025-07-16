class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        far = 0
        current_end = 0
        for i in range(len(nums)-1):
            far = max(far , i+nums[i])
            if i == current_end:
                jump+=1
                current_end = far 
        return jump
            

        