class Solution:
    def minimumSum(self, num: int) -> int:
        num_str = sorted(str(num))

        n = len(num_str)
        min_sum = 0

        for i in range(n // 2):
            min_sum += int(num_str[i] + num_str[n - 1 - i])

        return min_sum

        # # Pythonic refinement:
        # # Sort digits as strings
        # num_str = sorted(str(num))

        # # Form the two numbers using alternate digits
        # new1, new2 = ''.join(num_str[::2]), ''.join(num_str[1::2])

        # # Calculate the sum of the two numbers
        # return int(new1) + int(new2)
