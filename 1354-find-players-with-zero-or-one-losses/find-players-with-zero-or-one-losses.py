class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        checker = {}
        for i in matches:
            checker[i[0]] = checker.get(i[0],0)
            checker[i[1]] = checker.get(i[1],0) + 1       
 
        res = [[],[]]
        for num, wins in checker.items():
            if wins == 0:
                res[0].append(num)
            elif wins == 1:
                res[1].append(num)
        res[1].sort()
        res[0].sort()
        return res
