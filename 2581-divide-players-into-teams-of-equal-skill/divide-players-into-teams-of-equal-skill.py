class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        first = 0
        last = len(skill)-1
        res = 0
        products = skill[first] + skill[last]
        if len(skill) == 2:
            return skill[first]*skill[last]
        while first < last:
            x = skill[first] + skill[last]
            if x == products:
                res += skill[first] * skill[last]
                products = x
            else:
                return -1
            last-=1
            first+=1
        return res