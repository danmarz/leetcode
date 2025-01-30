class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # current_hours, current_minutes = current.split(":")
        # correct_hours, correct_minutes = correct.split(":")

        # # hours
        # current_hours = int(current_hours)
        # correct_hours = int(correct_hours)

        # # minutes
        # current_minutes = int(current_minutes)
        # correct_minutes = int(correct_minutes)

        # # convert hours into minutes, move calculations in minutes from now on
        # current = current_hours * 60 + current_minutes
        # correct = correct_hours * 60 + correct_minutes

        # difference = abs(current - correct)
        # ops = 0

        # while difference:
        #     if difference >= 60:
        #         ops += 1
        #         difference -= 60
        #     elif difference >= 15:
        #         ops += 1
        #         difference -= 15
        #     elif difference >= 5:
        #         ops += 1
        #         difference -= 5
        #     elif difference >= 1:
        #         ops += 1
        #         difference -= 1

        # return ops

        # Same line of thought but made much more concise (map() saves a lot of lines, so does step in [...])
        # Convert HH:MM format to total minutes
        def to_minutes(time):
            hh, mm = map(int, time.split(":"))
            return hh * 60 + mm

        # Compute time difference
        current_minutes = to_minutes(current)
        correct_minutes = to_minutes(correct)
        diff = correct_minutes - current_minutes

        # Apply the greedy approach
        count = 0
        for step in [60, 15, 5, 1]:  # Largest steps first
            count += diff // step  # How many times can we use this step?
            diff %= step  # Remaining minutes after using this step

        return count
