class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #  #  using counting sorting
        maxNum = max(heights)
        heightCount = [0]*(maxNum +1)
        namesCount = [0]*(maxNum +1)
        for num in range(len(names)):
            heightCount[heights[num]]+=1
            namesCount[heights[num]] = names[num]
        target = 0

        for index,value in enumerate(heightCount):
            for i in range(value):
                heights[target] = index
                names[target] = namesCount[index]
                target += 1
        
        return names[::-1]




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

        # # using selection sorting 
        # n = len(names)
        # for i in range(n):
        #     max_index = i
        #     for j in range(i+1,n):
        #         if heights[j] > heights[max_index]:
        #             max_index = j
        #     heights[i] , heights[max_index] = heights[max_index], heights[i]
        #     names[i],names[max_index] = names[max_index],names[i]    
        # return names

