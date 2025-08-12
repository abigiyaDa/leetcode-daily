class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # time o(n*m*log(nm))

        rows = len(heightMap)
        cols = len(heightMap[0])
        # add border to min heap
        # mark as visited  
        min_heap = []
        for i in range(rows):
            for j in range(cols):
                # check if the row i is [the 1st row ,or the last row]
                # or j (the column) is [the 1st column,or last column]
                if i in [0,rows-1] or j in [0,cols-1]:
                    #if so push to the min heap a 3 pair value 
                        #1 height of that position(heightMap[i][j]) and the 2 coordinates (i and j)
                    heappush(min_heap, (heightMap[i][j],i,j))
                    heightMap[i][j] = -1 # marking it visited 
        # 2. prioritize smallest heights.
        # maintain max height to calculate
        # water stored in each inner position
        res = 0
        max_h = -1

        while min_heap:
            h,r,c = heappop(min_heap)
            max_h = max(max_h,h)
            res += max_h - h

            # for that specific height h will go through its potential neighbors

            neighbors = [[r+1 ,c] , [r-1,c] , [r,c+1] , [r,c-1]]
            for nr,nc in neighbors:
                if (
                    nr < 0 or nc < 0 or
                    nr == rows or nc == cols or
                    heightMap[nr][nc] == -1
                ):
                    continue
                heappush(min_heap , (heightMap[nr][nc],nr,nc))
                heightMap[nr][nc] = -1 
        return res


