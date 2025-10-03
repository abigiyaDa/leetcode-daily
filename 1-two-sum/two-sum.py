class Solution(object):
    def twoSum(self, nums, target):
        #optimal solution
        # x = {}
        # for i,v in enumerate(nums):
        #     if(target - v in x):
        #         return [x[target - v],i]
        #     else:
        #         x[v] = i
        
        #creates pairs of (value, original_index): 
        # space 0(n)

        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()  
        left = 0
        right = len(nums)-1
        while left < right:
            current_sum = arr[left][0]+arr[right][0]
            if current_sum == target:
                return [arr[left][1],arr[right][1]]
            elif current_sum < target :
                left +=1
            else:
                right -= 1
            
            
        
            
        

        