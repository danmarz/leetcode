class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        ans = []
        ans.append(1)

        for i in range(rowIndex):
            ans = [0] + ans

            for j in range(len(ans) - 1):
                ans[j] = ans[j] + ans[j + 1]

        return ans
