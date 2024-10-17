class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Initialize starting point altitude
        current_altitude = 0
        # Variable to track the maximum altitude
        max_altitude = 0

        # Traverse through the gain array to compute altitudes
        for g in gain:
            # Update current altitude
            current_altitude += g
            # Update maximum altitude if the current one is higher
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
