class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            lineWords = []
            lineLen = 0
            while i < len(words) and lineLen + len(words[i]) +len(lineWords) <= maxWidth:
                lineWords.append(words[i])
                lineLen += len(words[i])
                i+=1
            # if last line or only one word the left justify
            if i == len(words) or len(lineWords) == 1:
                line = " ".join(lineWords)
                line+= " "*(maxWidth - len(line))
            else:
                spaces = maxWidth-lineLen
                gap = len(lineWords)-1
                spaceEach = spaces//gap
                extra = spaces % gap

                line = ""
                for j, word in enumerate(lineWords):
                    line += word
                    if j < gap:
                        line += " "*(spaceEach + (1 if j < extra else 0))
            res.append(line)
        return res