class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Check if rec1 is to the left of rec2 or if rec1 is to the right of rec2
        if rec1[2] <= rec2[0] or rec2[2] <= rec1[0]:
            return False

        # Check if rec1 is below rec2 or if rec1 is above rec2
        if rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
            return False

        # If none of the above conditions are met, the rectangles overlap
        return True
