class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = []

        # Find the minimum side in each rectangle (that can form the largest square)
        for rect in rectangles:
            largest = min(rect[0], rect[1])
            squares.append(largest)

        # Find the largest square[s]
        largest_square = max(squares)

        # Return the count of the largest square[s]
        return squares.count(largest_square)

        # ## Alternative, more efficient solution (only 1 loop)
        # # Initialize a variable to store the largest square's side length found so far.
        # max_len = 0
        # # Initialize a counter for rectangles that can form squares of the largest side length.
        # count = 0

        # # Loop through each rectangle in the list.
        # for l, w in rectangles:
        #     # Find the maximum square side length that can be cut from the current rectangle.
        #     square_side = min(l, w)

        #     # If the current square side length is larger than the max_len found so far:
        #     if square_side > max_len:
        #         # Update max_len and reset count as we have found a new largest side length.
        #         max_len = square_side
        #         count = 1
        #     # If the current square side length matches the max_len:
        #     elif square_side == max_len:
        #         # Increment the counter as another rectangle can form a square of this size.
        #         count += 1

        # # Return the total number of rectangles that can form squares of side length max_len.
        # return count
