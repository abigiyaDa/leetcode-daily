class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        teams=n//2
        skill.sort()
        left,right = 0,n-1
        target = skill[left]+skill[right]
        res = []
        while left < right:
            if skill[left]+skill[right] == target:
                res.append(skill[left]*skill[right])
                left+=1
                right-=1
            else:
                return -1
        return sum(res)

        