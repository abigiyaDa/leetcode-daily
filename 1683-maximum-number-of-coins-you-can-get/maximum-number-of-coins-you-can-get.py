class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)//3 #We’ll play n rounds (each round consumes 3 piles).
        res = 0
        piles.sort(reverse=True)

        for i in range(1,2*n,2):
            res += piles[i]
        return res


