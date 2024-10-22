class Solution:
    def check(self, nums: List[int]) -> bool:
        # Count the number of times we find a decreasing pair
        count_decreasing = 0
        n = len(nums)

        # Traverse the array and count the number of decreases
        for i in range(n):
            # Compare current element with the next (mod n to account for wrap-around)
            if nums[i] > nums[(i + 1) % n]:
                count_decreasing += 1
                # If more than one decreasing pair, it's not a rotated sorted array
                if count_decreasing > 1:
                    return False

        # If the array is either sorted or sorted and rotated, return True
        return True
