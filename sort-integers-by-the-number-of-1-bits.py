class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Custom sorting key
        def sort_key(x):
            return (bin(x).count("1"), x)

        # Sort the array using the custom key
        return sorted(arr, key=sort_key)
