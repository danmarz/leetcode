class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        # Add the current request time to the list
        self.requests.append(t)

        # Remove requests that fall outside the time window [t - 3000, t]
        while self.requests[0] < t - 3000:
            self.requests.pop(0)

        # Return the number of requests within the time window
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
