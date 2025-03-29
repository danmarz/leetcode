class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # result = 0
        # while grid[0]:
        #     removed = []
        #     for row in grid:
        #         max_element = max(row)
        #         row.remove(max_element)
        #         removed.append(max_element)
        #     result += max(removed)
        # return result

        # Improved efficiency: sort once: O(m * n log n), then loop to get the largest element in O(m * n) time
        # Step 1: Sort each row descending once
        for row in grid:
            row.sort(reverse=True)

        total = 0
        # Step 2: Iterate column by column
        for col in range(len(grid[0])):  # Each column corresponds to a round
            max_val = 0
            for row in grid:
                max_val = max(max_val, row[col])
            total += max_val

        return total
