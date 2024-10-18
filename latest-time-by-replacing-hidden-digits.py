class Solution:
    def maximumTime(self, time: str) -> str:
        # Split the time into hours and minutes parts
        hour, minute = time.split(":")

        # Handle the hour part
        if hour[0] == "?":
            # If the second hour digit is between 0 and 3, we can use 2 for the first digit
            # Otherwise, we use 1
            if hour[1] == "?" or hour[1] < "4":
                hour = "2" + hour[1]
            else:
                hour = "1" + hour[1]

        if hour[1] == "?":
            # If the first hour digit is 2, the second digit can be at most 3
            if hour[0] == "2":
                hour = hour[0] + "3"
            else:
                hour = hour[0] + "9"

        # Handle the minute part
        if minute[0] == "?":
            minute = "5" + minute[1]

        if minute[1] == "?":
            minute = minute[0] + "9"

        # Join the hour and minute to form the latest valid time
        return f"{hour}:{minute}"
