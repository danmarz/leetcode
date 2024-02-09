class MyHashSet:
    # set method (faster)
    def __init__(self):
        self.ls = set()

    def add(self, key: int) -> None:
        self.ls.add(key)

    def remove(self, key: int) -> None:
        if key in self.ls:
            self.ls.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.ls

    # list method
    """
    def __init__(self):
        self.vals = list()

    def add(self, key: int) -> None:
        self.vals.append(key)

    def remove(self, key: int) -> None:
        self.vals = [y for y in self.vals if y != key]

    def contains(self, key: int) -> bool:
        for val in self.vals:
            if val == key:
                return True
        return False
    """


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
