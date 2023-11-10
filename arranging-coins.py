class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Initialize pointers to first and last possible row lengths
        left, right = 1, n

        while left <= right:
            # Compute the midpoint between left and right
            mid = left + (right - left) // 2

            # Compute the total number of coins needed for mid complete rows
            coins = (mid * (mid + 1)) // 2

            # If we have enough coins, look for a smaller number of rows
            if coins <= n:
                left = mid + 1
            # Otherwise, look for a larger number of rows
            else:
                right = mid - 1

        # Return the number of complete rows (i.e., right pointer)
        return right

        """ Alternative binary search:
        ans= bisect_left(range(1,n),n,key=lambda x:x*(x+1)//2)+1
        if ans*(ans+1)//2==n:
            return ans
        return ans-1
        """

        """ Brute force solution:
        row = 0
        while n - row > 0:
            row += 1
            n -= row
            
        return row
        """
