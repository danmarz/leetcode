class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create an empty set to store seen values

        for num in nums:
            if num in seen:
                return True  # If the number is already in the set, it's a duplicate
            seen.add(num)  # Otherwise, add it to the set

        return False  # If the loop completes without finding duplicates, return False
