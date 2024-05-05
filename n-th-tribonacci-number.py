class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Initialize the array to store the Tribonacci sequence
        tribonacci_seq = [0] * (n + 1)
        tribonacci_seq[1] = tribonacci_seq[2] = 1

        # Calculate the Tribonacci sequence up to the nth term
        for i in range(3, n + 1):
            tribonacci_seq[i] = (
                tribonacci_seq[i - 1] + tribonacci_seq[i - 2] + tribonacci_seq[i - 3]
            )

        return tribonacci_seq[n]
