class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count("1")  # Step 1: Count the total number of ones
        max_score = 0
        left_zeros = 0
        right_ones = total_ones

        # Step 3: Iterate through the string for possible split points
        for i in range(len(s) - 1):
            if s[i] == "0":
                left_zeros += 1
            else:
                right_ones -= 1

            current_score = left_zeros + right_ones
            max_score = max(max_score, current_score)

        return max_score
