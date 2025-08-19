class Solution:
    def reverseWords(self, s: str) -> str:
        # parse 
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

        # while i < n:
        #     # skip spaces
        #     while i < n and s[i] == " ":
        #         i += 1
        #     if i >= n:   # end of string
        #         break
        #     # find end of word
        #     r = i
        #     while r < n and s[r] != " ":
        #         r += 1
        #     # collect the word
        #     words.append(s[i:r])

        #     # move i to r (next word)
        #     i = r
        words.reverse()
        return " ".join(words)



        # # space o(n) and time o(n)
        # s=s.strip().split()
        # s.reverse()
        # return " ".join(s)





        
        