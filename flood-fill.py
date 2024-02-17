class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # Store the color of the starting pixel
        startColor = image[sr][sc]

        # If the new color is the same as the starting color, no need to perform flood fill
        if startColor == color:
            return image

        # Initialize a stack to perform iterative DFS
        stack = [(sr, sc)]

        # Define the directions (up, down, left, right) to explore neighboring pixels
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Perform iterative DFS until the stack is empty
        while stack:
            # Pop the current pixel from the stack
            row, col = stack.pop()

            # Fill the current pixel with the new color
            image[row][col] = color

            # Explore neighboring pixels
            for dr, dc in directions:
                # Calculate the coordinates of the neighboring pixel
                r, c = row + dr, col + dc

                # Check if the neighboring pixel is within the image boundaries and has the same color as the starting pixel
                if (
                    0 <= r < len(image)
                    and 0 <= c < len(image[0])
                    and image[r][c] == startColor
                ):
                    # Add the neighboring pixel to the stack for further exploration
                    stack.append((r, c))
                    # Fill the neighboring pixel with the new color
                    image[r][c] = color

        # Return the modified image after flood fill
        return image
