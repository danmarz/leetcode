# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                # If mid is a bad version, search in the left half.
                right = mid
            else:
                # If mid is not a bad version, search in the right half.
                left = mid + 1

        # At the end of the loop, left will be the first bad version.
        return left
