class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Dictionary to count the occurrences of each sum of digits
        sum_count = defaultdict(int)

        # Helper function to calculate the sum of digits
        def digit_sum(x):
            return sum(int(digit) for digit in str(x))

        # Populate the dictionary with counts of each sum of digits
        for num in range(1, n + 1):
            s = digit_sum(num)
            sum_count[s] += 1

        # Find the maximum count value
        max_count = max(sum_count.values())

        # Count how many groups have the maximum size
        largest_group_count = sum(
            1 for count in sum_count.values() if count == max_count
        )

        return largest_group_count
