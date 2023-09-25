from random import sample

class RandomizedSet:
    def __init__(self):
        self.rand_set = set()

    def insert(self, val: int) -> bool:
        if val in self.rand_set:
            return False
        self.rand_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.rand_set:
            return False
        self.rand_set.remove(val)
        return True

    def getRandom(self) -> int:
        return sample(self.rand_set,1)[0]