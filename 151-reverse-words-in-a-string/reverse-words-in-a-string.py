class Solution:
    def reverseWords(self, s: str) -> str: 
        words = []
        n = len(s)
        i = 0
        start = 0

        while i < n:
            if s[i] != " ":
                start = i
                while i < n and s[i] != " ":
                    i+=1
                words.append(s[start:i])
            i+=1
        words.reverse()
        return " ".join(words)



        # # space o(n) and time o(n)
        # s=s.strip().split()
        # s.reverse()
        # return " ".join(s)





        
        