class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        
        for size in range(n, 1, -1):#(start,end,steps)-starts from the end
            # 1. Find index of the max number in arr[0:size]
            maxi = max(arr[0:size]) # from 0 to i
            max_index = arr.index(maxi)
            
            if max_index == size - 1: #if the max number is in the last position
                continue  # already in correct position
            
            # 2. Flip max to the front if not already there
            if max_index != 0:
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
                res.append(max_index + 1)
            
            # 3. Flip it to its correct position
            arr[:size] = reversed(arr[:size])
            res.append(size)
        
        return res


            

        