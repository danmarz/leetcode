class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Create a list to store the number of soldiers and corresponding row index
        soldier_count = []
        
        # Iterate through each row in the matrix
        for index, row in enumerate(mat):
            # Count the number of soldiers (1's) in the row
            count = sum(row)
            # Append a tuple of (number of soldiers, row index) to the list
            soldier_count.append((count, index))
        
        # Sort the list based on the number of soldiers and then by row index
        soldier_count.sort()
        
        # Extract the indices of the first k elements from the sorted list
        weakest_rows = [index for _, index in soldier_count[:k]]
        
        return weakest_rows