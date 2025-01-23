class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []
        start, end = s.split(":")
        start_col, start_row = start[0], start[1]
        end_col, end_row = end[0], end[1]

        while start_col <= end_col:
            while start_row <= end_row:
                result.append(str(start_col) + str(start_row))
                start_row = chr(ord(start_row) + 1)
            start_row = start[1]
            start_col = chr(ord(start_col) + 1)

        return result
