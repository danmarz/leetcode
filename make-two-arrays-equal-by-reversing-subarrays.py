class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Sort both target and arr
        # Sorting is a common approach in such problems because reversing any subarray
        # will only affect the order of elements, not their values.
        target.sort()
        arr.sort()

        # After sorting, if target and arr are equal, it means that arr can be made equal to target
        # through some series of reverse operations on subarrays.
        return target == arr
