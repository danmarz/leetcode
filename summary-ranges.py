class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return (
                []
            )  # If the input list is empty, return an empty list as there are no ranges to create.

        ranges = []  # Initialize an empty list to store the ranges.
        start = end = nums[0]  # Initialize start and end to the first element of nums.

        for num in nums[1:]:  # Iterate through the remaining elements of nums.
            if num == end + 1:
                # If num is consecutive with the current range, update the end of the range.
                end = num
            else:
                # If num is not consecutive, add the current range to ranges and start a new range.
                if start == end:
                    # If start and end are the same, it's a single number range.
                    ranges.append(str(start))
                else:
                    # If start and end are different, it's a range of numbers (a->b format).
                    ranges.append(str(start) + "->" + str(end))
                start = end = num  # Start a new range with num.

        if start == end:
            # After the loop, there might be one more single number range to add.
            ranges.append(str(start))
        else:
            # If start and end are different, add the last range.
            ranges.append(str(start) + "->" + str(end))

        return ranges  # Return the list of formatted ranges.

        """  # Alternative solution
        ranges = [] # [start, end] or [x, y]
        for i, n in enumerate(nums):
            if ranges and ranges[-1][1] == n-1:
                ranges[-1][1] = n
            else:
                ranges.append([n, n])
        
        return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]
        """
