class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rowOnes = 0
        maxRow = 0
        for row in range(len(mat)):
            currentRowOnes = sum(mat[row])  # Directly sum the row, only 1s count
            if currentRowOnes > rowOnes:
                rowOnes = currentRowOnes
                maxRow = row
        return [maxRow, rowOnes]
