class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = sorted(strs, key=len)[0]

        for j in range(len(shortest_string)):
            for s in strs:
                if s[j] != shortest_string[j]:
                    return shortest_string[:j]
                
        return shortest_string
        