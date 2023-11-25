class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrt_area = int(area**0.5)  # Calculate the square root of the area

        while area % sqrt_area != 0:
            sqrt_area -= 1

        return [area // sqrt_area, sqrt_area]
