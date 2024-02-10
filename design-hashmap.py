class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key: int) -> int:
        """
        Hash function to map keys to indices.
        """
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        """
        Inserts a (key, value) pair into the HashMap.
        If the key already exists, update the corresponding value.
        """
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                self.table[hash_key][i] = (key, value)
                return
        self.table[hash_key].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key.
        """
        hash_key = self._hash(key)
        for k, v in self.table[hash_key]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the key and its corresponding value if the map contains the mapping for the key.
        """
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                del self.table[hash_key][i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
