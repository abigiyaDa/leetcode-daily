class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # # using insertion sorting 
        # n=len(names)
        # for i in range(1,n):
        #     key_height = heights[i]
        #     key_name = names[i]
        #     j=i-1
        #     while j>=0 and heights[j]<key_height:
        #         heights[j+1] = heights[j]
        #         names[j+1]=names[j]
        #         j-=1#important 
        #     heights[j+1]=key_height
        #     names[j+1]=key_name    
        # return names

        # # using bubble sort
        # n = len(names)
        # for i in range(n):
        #     for j in range(1,n-i):
        #         if heights[j] > heights[j-1]:
        #             heights[j] , heights[j-1] = heights[j-1],heights[j]
        #             names[j],names[j-1] = names[j-1],names[j]
        # return names

        # using selection sorting 
        n = len(names)
        for i in range(n):
            max_index = i
            for j in range(i+1,n):
                if heights[j] > heights[max_index]:
                    max_index = j
            heights[i] , heights[max_index] = heights[max_index], heights[i]
            names[i],names[max_index] = names[max_index],names[i]    
        return names

