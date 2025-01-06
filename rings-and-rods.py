class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        color = ""

        for i in range(len(rings)):
            if i % 2 != 0:
                if rings[i] not in rods:
                    rods[rings[i]] = color
                else:
                    rods[rings[i]] += color
            else:
                color = rings[i]

        return sum(
            1
            for rod in rods
            if "R" in rods[rod] and "G" in rods[rod] and "B" in rods[rod]
        )

        # # Optimized solution using a set instead of a dict
        # rods = {str(i): set() for i in range(10)}  # Initialize a set for each rod

        # # Populate the rods dictionary
        # for i in range(0, len(rings), 2):
        #     color = rings[i]
        #     rod = rings[i + 1]
        #     rods[rod].add(color)

        # # Count rods containing all three colors
        # return sum(1 for rod in rods.values() if len(rod) == 3)
