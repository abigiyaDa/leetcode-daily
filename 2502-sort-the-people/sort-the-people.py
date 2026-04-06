class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # insertion sorting 
        size = len(names)
        for i in range(1,size):
            key_h = heights[i]
            key_n = names[i]
            j= i-1
            while j >= 0 and key_h > heights[j]:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j] 
                j -= 1
            names[j+1] = key_n
            heights[j+1] = key_h
        return names
        # # selection sorting time o(n^2) space 0(1)
        # size = len(names)
        # for i in range(size):
        #     min_idx = i
        #     for j in range(i+1,size):
        #         if heights[min_idx] < heights[j]:
        #             min_idx = j
        #     heights[i] ,heights[min_idx]= heights[min_idx], heights[i]
        #     names[i],names[min_idx] = names[min_idx] , names[i]
        # return names
        # # bubble sorting time o(n^2) space 0(1)
        # size = len(names)
        # for i in range(size):
        #     for j in range(size - i-1):
        #         if heights[j] < heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             names[j],names[j+1] = names[j+1] , names[j]
        # return names

        