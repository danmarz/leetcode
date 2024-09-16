class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # Initialize the available slots for each car type
        self.slots = {
            1: big,  # Big car slots
            2: medium,  # Medium car slots
            3: small,  # Small car slots
        }
        # Reminder: Dictionary maps carType to available slots

    def addCar(self, carType: int) -> bool:
        # Check if there are slots available for the given carType
        if self.slots[carType] > 0:
            # If available, park the car by decrementing the slot count
            self.slots[carType] -= 1
            # Reminder: Update the slot count after parking
            return True  # Successfully parked
        else:
            # No slots available for this carType
            return False  # Cannot park the car


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
