class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        result = [] 
        while i<len(nums)-2:
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                current_sum = nums[i] + nums[j]+nums[k]
                if current_sum == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    # skip duplicates-find unique i and j
                    while j<k and nums[j] == nums[j+1]:
                        j+=1
                    while j<k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    j+=1
                    k-=1
                elif current_sum<0:
                    j+=1
                else:
                    k-=1         
            i+=1
        return result

    


        