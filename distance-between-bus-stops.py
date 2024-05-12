class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        n = len(distance)
        total_distance = sum(distance)
        clockwise_distance = 0
        counterclockwise_distance = 0

        # Calculate clockwise distance
        current_stop = start
        while current_stop != destination:
            clockwise_distance += distance[current_stop]
            current_stop = (current_stop + 1) % n

        # Calculate counterclockwise distance
        current_stop = start
        while current_stop != destination:
            current_stop = (current_stop - 1) % n
            counterclockwise_distance += distance[current_stop]

        # Return the minimum distance
        return min(clockwise_distance, counterclockwise_distance)
