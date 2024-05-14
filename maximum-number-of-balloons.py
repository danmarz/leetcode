class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Define the target word "balloon"
        target = "balloon"

        # Count occurrences of characters in text
        text_count = {}
        for char in text:
            text_count[char] = text_count.get(char, 0) + 1

        # Count occurrences of characters in "balloon"
        balloon_count = {}
        for char in target:
            balloon_count[char] = balloon_count.get(char, 0) + 1

        # Initialize the maximum number of instances of "balloon"
        max_instances = float("inf")

        # Calculate the maximum number of instances based on character counts
        for char in balloon_count:
            # If the character does not exist in text, return 0 instances
            if char not in text_count:
                return 0
            # Calculate the maximum instances based on character counts
            max_instances = min(max_instances, text_count[char] // balloon_count[char])

        return max_instances
