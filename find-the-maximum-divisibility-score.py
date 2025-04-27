class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_score = -1  # Initialize the highest score found
        best_divisor = None  # Initialize the best divisor

        for divisor in divisors:
            score = 0  # Reset the score for the current divisor

            for num in nums:
                # Check if the current num is divisible by the current divisor
                if num % divisor == 0:
                    score += 1  # Increment score if divisible

            # Update the best divisor if we find a higher score
            if score > max_score:
                max_score = score
                best_divisor = divisor
            # If same score but smaller divisor, update as well
            elif score == max_score:
                best_divisor = min(best_divisor, divisor)

        return best_divisor
