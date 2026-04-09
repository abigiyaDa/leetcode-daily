class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        round = n//3
        res = 0
        piles.sort()
        for i in range(n-2,round-1,-2):
            res += piles[i]
        return res