class Solution(object):
    def twoSum(self, nums, target):
        x = {} # Dictionary to store the value and its index
        for i,v in enumerate(nums): # Enumerate gives us both index and value
            # Check if the complement (target - v) exists in the dictionary
            if(target - v in x): 
                # If it exists, return the indices of the two numbers
                # The first index is from the dictionary, the second is the current index
                return [x[target - v],i]
            else:
                # If it does not exist, store the current value and its index in the dictionary
                x[v] = i
        # If no solution is found, return an empty list
        return []