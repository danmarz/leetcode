class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        # Define the thresholds
        bulky_dimension_threshold = 10**4  # 10,000
        bulky_volume_threshold = 10**9  # 1,000,000,000
        heavy_mass_threshold = 100  # Mass threshold for "Heavy"

        # Calculate volume
        volume = length * width * height

        # Check for bulky condition
        is_bulky = (
            length >= bulky_dimension_threshold
            or width >= bulky_dimension_threshold
            or height >= bulky_dimension_threshold
            or volume >= bulky_volume_threshold
        )

        # Check for heavy condition
        is_heavy = mass >= heavy_mass_threshold

        # Return the correct category based on the conditions
        if is_bulky and is_heavy:
            return "Both"
        elif is_bulky:
            return "Bulky"
        elif is_heavy:
            return "Heavy"
        else:
            return "Neither"
