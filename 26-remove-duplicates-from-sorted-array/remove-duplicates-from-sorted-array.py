class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        b = a+1
        c = len(nums)-1
        while b<=c:
            if nums[a] != nums[b]:
                nums[a+1] = nums[b]
                a+=1
            b+=1
        return a+1

