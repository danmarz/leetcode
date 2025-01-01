class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # if len(colors) == 2:
        #     return 1

        # mid = len(colors) // 2
        # maxD = 0

        # for i in range(mid):
        #     for j in range(len(colors) - 1, mid, -1):
        #         if colors[i] != colors[j]:
        #             maxD = max(maxD, abs(j - i))
        #         elif colors[i] != colors[mid] or colors[j] != colors[mid]:
        #             maxD = max(maxD, max(abs(j - mid), abs(i - mid)))

        # return maxD

        # Optimized, O(n) solution
        n = len(colors)
        max_dist = 0

        # Compare the leftmost house with houses on the right
        for j in range(n - 1, -1, -1):
            if colors[0] != colors[j]:
                max_dist = max(max_dist, abs(0 - j))
                break

        # Compare the rightmost house with houses on the left
        for i in range(n):
            if colors[n - 1] != colors[i]:
                max_dist = max(max_dist, abs(n - 1 - i))
                break

        return max_dist
