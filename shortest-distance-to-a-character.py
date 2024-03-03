class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # Initialize an array to store the distances
        distances = []

        # Initialize variables to track the index of the last occurrence of character c
        last_occurrence = float("-inf")

        # Iterate through the string from left to right to find distances to the left
        for i in range(len(s)):
            if s[i] == c:
                last_occurrence = i
            distances.append(i - last_occurrence)

        # Reset last_occurrence to track the index of the last occurrence of character c from right to left
        last_occurrence = float("inf")

        # Iterate through the string from right to left to find distances to the right
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                last_occurrence = i
            distances[i] = min(distances[i], last_occurrence - i)

        return distances
