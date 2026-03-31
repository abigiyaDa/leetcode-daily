class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # optimal 
        winner = 0  # 0-indexed
        for i in range(2, n+1):
            winner = (winner + k) % i
        return winner + 1  # convert to 1-indexed

        
        # # not efficent complexity = o(n^2), while loop[o(n-1) = o(n)] * pop = o(n) for at nay index
        # res = [i for i in range(1, n+1)]
        # idx = 0
        # while len(res) > 1:
        #     idx = (idx + k - 1) % len(res)  # k-th person to remove
        #     res.pop(idx)
        # return res[0]

        