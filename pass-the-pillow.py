class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Each full back-and-forth takes 2 * (n - 1) seconds
        cycle_len = 2 * (n - 1)
        print(cycle_len)

        # We only care about time within the current cycle
        time %= cycle_len
        print(time)

        # If still moving forward (before reaching nth person)
        if time < n - 1:
            return 1 + time  # Forward from 1
        else:
            return n - (time - (n - 1))  # Backward from n
