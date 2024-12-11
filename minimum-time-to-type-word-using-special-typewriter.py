class Solution:
    def minTimeToType(self, word: str) -> int:
        # Initialize time and the starting position of the pointer ('a')
        time = 0
        current_char = "a"

        for target_char in word:
            # Calculate the absolute distance in the alphabet
            distance = abs(ord(target_char) - ord(current_char))
            # Compute the circular distance
            circular_distance = min(distance, 26 - distance)
            # Update time (time to move + time to type)
            time += circular_distance + 1  # 1 second to type
            # Update the current pointer position
            current_char = target_char

        return time
