import random
class RandomizedSet:

    def __init__(self):
        self.size = 0
        self.idx_to_val = {}
        self.val_to_idx = {}


    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        else:
            self.val_to_idx[val] = self.size
            self.idx_to_val[self.size] = val
            self.size += 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        else:
            cur_idx = self.val_to_idx[val]
            good_val = self.idx_to_val[self.size - 1]
            self.idx_to_val[cur_idx] = good_val
            self.val_to_idx[good_val] = cur_idx

            self.val_to_idx.pop(val)
            self.idx_to_val.pop(self.size-1)
            self.size -= 1
            return True

    def getRandom(self) -> int:
        n = random.randrange(self.size)
        return self.idx_to_val[n]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()