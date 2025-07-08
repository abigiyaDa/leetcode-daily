class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #soln 2 good time o(n) and space o(1)
        # normalize k, for k > len(nums) -otherwise, it will break
        k %= len(nums)
        def reverse(start,end):
            while start<end:
                nums[start],nums[end] = nums[end],nums[start]
                start +=1
                end -=1
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)

        #solution 1 but time complexity is o(n+k) and not scalable 
        # count = 0
        # lastIndex = len(nums)-1
        # while count < k:
        #     nums.insert(0,nums[lastIndex])
        #     count +=1
        #     nums.pop()
        # return nums 
        

        
        