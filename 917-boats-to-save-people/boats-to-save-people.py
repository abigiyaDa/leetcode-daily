class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        size = len(people)
        left,right = 0, size-1
        people.sort()
        count=0
        while left<=right:
            if people[left]+people[right] > limit:
                count +=1
                right -=1
            else:
                count+=1
                left+=1
                right-=1
        return count

        