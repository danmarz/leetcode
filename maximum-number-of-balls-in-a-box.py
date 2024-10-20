class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box_counts = {}  # Dictionary to store the count of balls in each box.

        for ball in range(lowLimit, highLimit + 1):
            box_number = sum(
                int(digit) for digit in str(ball)
            )  # Calculate the sum of digits.
            if box_number in box_counts:
                box_counts[box_number] += 1
            else:
                box_counts[box_number] = 1

        # Find the maximum number of balls in any box.
        return max(box_counts.values())
