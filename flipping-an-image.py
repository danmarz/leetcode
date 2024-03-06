class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []

        for line in image:
            new_line = []
            for i in range(len(line) - 1, -1, -1):
                new_line.append(int(not line[i]))
            result.append(new_line)

        return result

        # Alternative solution
        """
        ans = []

        for row in image:
            newRow = row[::-1]
            for pos,char in enumerate(newRow):
                if char == 0:
                    newRow[pos] = 1
                else:
                    newRow[pos] = 0
            ans.append(newRow)

        return ans
        """
