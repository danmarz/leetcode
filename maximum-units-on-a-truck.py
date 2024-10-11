class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort the box types by units per box in descending order
        sorted_boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        units = 0
        for numberOfBoxes, unitsPerBox in sorted_boxes:
            if truckSize == 0:
                break  # Stop if the truck is already full

            # Calculate how many boxes to take (either all or just enough to fill the truck)
            boxes_to_take = min(truckSize, numberOfBoxes)

            # Add units to the total
            units += boxes_to_take * unitsPerBox

            # Decrease the remaining capacity of the truck
            truckSize -= boxes_to_take

        return units
