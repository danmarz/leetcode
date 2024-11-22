class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """Check if mat can be rotated to match target."""
        for _ in range(4):  # Try all four rotations
            if mat == target:
                return True
            # Rotate mat 90 degrees clockwise
            mat = [list(row) for row in zip(*mat[::-1])]
        return False

        return can_transform(mat, target)
