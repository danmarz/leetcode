class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        # Initialize an empty list to store the intervals of large groups
        large_groups = []

        # Initialize variables to track the start and end indices of the current group
        start = 0
        end = 0

        # Iterate through the string
        for i in range(1, len(s)):
            # If the current character is different from the previous one
            if s[i] != s[i - 1]:
                # Check if the current group is large (has 3 or more characters)
                if end - start >= 2:
                    large_groups.append([start, end])
                # Update the start index of the next group
                start = i
            # Update the end index of the current group
            end = i

        # Check if the last group is large
        if end - start >= 2:
            large_groups.append([start, end])

        return large_groups
