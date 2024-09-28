class OrderedStream:

    def __init__(self, n: int):
        # Initialize the stream with n slots set to None
        self.stream = [None] * n
        # Pointer to track the smallest unprocessed idKey
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        # Insert the value at the correct position
        self.stream[idKey - 1] = value

        # Initialize a list to store the result chunk
        chunk = []

        # Process consecutive values starting from ptr
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            chunk.append(self.stream[self.ptr])
            self.ptr += 1

        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
