class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # Initial values for the longest keypress
        longest_duration = releaseTimes[0]
        longest_key = keysPressed[0]

        # Iterate through the rest of the keysPressed array
        for i in range(1, len(keysPressed)):
            # Calculate the duration of the current keypress
            duration = releaseTimes[i] - releaseTimes[i - 1]

            # If current duration is longer, or it's equal but key is lexicographically larger
            if duration > longest_duration or (
                duration == longest_duration and keysPressed[i] > longest_key
            ):
                longest_duration = duration
                longest_key = keysPressed[i]

        return longest_key
