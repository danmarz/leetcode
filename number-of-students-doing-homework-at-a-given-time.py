class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        # Initialize a counter to count the number of students doing homework at queryTime
        count = 0

        # Iterate through the lists of start and end times
        for i in range(len(startTime)):
            # Check if the queryTime falls within the start and end time (inclusive) for each student
            if startTime[i] <= queryTime <= endTime[i]:
                # If true, increment the counter
                count += 1

        # Return the final count of students doing homework at queryTime
        return count
