class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Get the dimensions of the image matrix
        rows, cols = len(img), len(img[0])

        # Define a helper function to calculate the average value for a pixel
        def average_value(r, c):
            total, count = 0, 0

            # Define the boundaries for the neighboring pixels
            top = max(0, r - 1)
            bottom = min(rows, r + 2)
            left = max(0, c - 1)
            right = min(cols, c + 2)

            # Iterate over the neighboring pixels and calculate the sum and count
            for row in range(top, bottom):
                for col in range(left, right):
                    total += img[row][col]
                    count += 1

            # Calculate and return the average value for the pixel
            return total // count

        # Apply the average function to each pixel in the image matrix
        return [[average_value(r, c) for c in range(cols)] for r in range(rows)]

        # Alternative solution
        """
        # Get the number of rows and columns in the image
        rows, cols = len(img), len(img[0])
        
        # Initialize a new matrix to store the smoothed image
        smoothed_img = [[0] * cols for _ in range(rows)]
        
        # Define directions for 8 neighboring cells
        directions = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
        
        # Iterate through each cell in the original image
        for i in range(rows):
            for j in range(cols):
                # Initialize variables to calculate the sum and count of neighboring cells
                total_sum = 0
                count = 0
                
                # Iterate through neighboring cells
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    
                    # Check if the neighboring cell is within the bounds of the image
                    if 0 <= ni < rows and 0 <= nj < cols:
                        total_sum += img[ni][nj]
                        count += 1
                
                # Calculate the average and update the smoothed image
                smoothed_img[i][j] = total_sum // count
        
        return smoothed_img
        """
