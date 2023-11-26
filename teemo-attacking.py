class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total_duration = (
            duration  # Initialize total duration with the duration of the first attack
        )

        for i in range(1, len(timeSeries)):
            diff = (
                timeSeries[i] - timeSeries[i - 1]
            )  # Calculate the time difference between consecutive attacks
            total_duration += min(
                diff, duration
            )  # Add the minimum of duration or time difference to total duration

        return total_duration
