from bisect import insort


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize the class variables
        self.k = k
        self.sorted_list = []
        # Add the initial elements to the sorted list
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Insert the new value into the sorted list
        insort(self.sorted_list, val)
        # If the size of the sorted list exceeds k, remove the smallest element
        if len(self.sorted_list) > self.k:
            self.sorted_list.pop(0)
        # Return the kth largest element, which is the first element in the sorted list
        return self.sorted_list[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
