class RandomizedSet:
    def __init__(self):
        self.my_dict= {}
        self.keys = []
        

    def insert(self, val: int) -> bool:
        if val not in self.my_dict:
            self.my_dict[val] = len(self.keys) 
            self.keys.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.my_dict:
            # find index of val from dict 
            idx = self.my_dict[val]
            # find last element from the list
            last_val = self.keys[-1]

            #swap val with last element
            #-so the last element is in the place of val and remove the last element 
            self.keys[idx] = last_val
            #update the dict so that the last val has the index of val 
            self.my_dict[last_val] = idx

            # remove last element 
            self.keys.pop()
            del self.my_dict[val]
            return True
        return False
        

    def getRandom(self) -> int:
        if self.keys :
            return random.choice(self.keys)
        return []
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()