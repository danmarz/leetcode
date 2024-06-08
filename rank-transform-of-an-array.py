class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Find the sorted list of unique elements
        sorted_unique_elements = sorted(set(arr))

        # Step 2: Create a rank mapping
        rank_map = {
            element: rank + 1 for rank, element in enumerate(sorted_unique_elements)
        }

        # Step 3: Replace each element in the original array with its rank
        ranked_arr = [rank_map[element] for element in arr]

        return ranked_arr
