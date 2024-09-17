class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # This optimized approach only needs to sort the array once and then check each element in a single loop pass,
        # leading to O(n log n) time complexity.

        # Step 1: Sort the array in descending order
        nums.sort(reverse=True)
        n = len(nums)

        # Step 2: Iterate over possible values of x
        for x in range(1, n + 1):
            # Check if the x-th largest element is >= x
            if nums[x - 1] >= x:
                # Step 3: If x is the last element or the next element is less than x
                if x == n or nums[x] < x:
                    return x
        # Step 4: If no special number is found, return -1
        return -1

        # This approach iterates through the array multiple times (one loop for each x), leading to an O(n²) time complexity.
        # When working with small arrays, the difference might not be noticeable, but as the input size grows, the optimized
        # approach (O(n log n)) will always outperform the quadratic solution.

        # Step 1: Sort the array in ascending order
        nums.sort()

        # Get the length of the array
        n = len(nums)

        # Step 2: Iterate over all possible values of x (from 0 to n)
        for x in range(n + 1):
            # Step 3: Check how many elements are greater than or equal to x
            # We can do this by comparing x with the elements in the sorted array
            # We know that if the length of nums is n, then the number of elements >= x
            # is the portion of the array starting from the first element that is >= x.
            greater_or_equal_count = 0

            # Step 4: Count the number of elements >= x
            # for num in nums:
            #     if num >= x:
            #         greater_or_equal_count += 1

            for pos, num in enumerate(nums):
                if num >= x:
                    greater_or_equal_count += len(nums[pos:])
                    break
            # print(x, greater_or_equal_count)

            # Step 5: If exactly x elements are greater than or equal to x, return x
            if greater_or_equal_count == x:
                return x

        # Step 6: If no such x is found, return -1
        return -1
