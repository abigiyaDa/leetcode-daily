class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        for num in range(left , right + 1):
            for i,j in ranges :
                if i <= num <= j:
                    break
            else: # if we go through all the elements in range and if it doesnt break return false bc its not covered in the range 
                return False 
        return True
        
        