class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index_map = {val: i for i, val in enumerate(arr2)}

        def custom_sort(x):
            # If x is in arr2, return its index; otherwise, return a large value
            return index_map.get(x, len(arr2) + x)

        # Sort arr1 using the custom sorting function
        arr1.sort(key=custom_sort)
        return arr1
