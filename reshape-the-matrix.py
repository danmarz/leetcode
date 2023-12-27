class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Check if reshape operation is possible
        if r * c != len(mat) * len(mat[0]):
            return mat  # Return original matrix if reshape not possible

        # Reshape the matrix
        reshaped = []
        elements = [elem for row in mat for elem in row]  # Flatten the matrix

        # Fill the reshaped matrix
        for i in range(0, len(elements), c):
            reshaped.append(elements[i : i + c])

        return reshaped  # Return the reshaped matrix
