class Solution:
    def countTime(self, time: str) -> int:
        # if not "?" in time:
        #     return 1

        # hours, minutes = time.split(":")

        # count_hours = 0
        # count_minutes = 0

        # if hours[0] == "?" and hours[1] == "?":
        #     count_hours += 24

        # elif hours[0] == "?":
        #     if int(hours[1]) < 4:
        #         count_hours += 3
        #     else:
        #         count_hours += 2

        # elif hours[1] == "?":
        #     if int(hours[0]) < 2:
        #         count_hours += 10
        #     elif int(hours[0]) == 2:
        #         count_hours += 4

        # if minutes[0] == "?" and minutes[1] == "?":
        #     count_minutes += 60

        # elif minutes[0] == "?":
        #     count_minutes += 6

        # elif minutes[1] == "?":
        #     count_minutes += 10

        # if count_hours and count_minutes:
        #     return count_hours * count_minutes
        # else:
        #     return max(count_hours, count_minutes)

        # Optimized solution:
        hours, minutes = time.split(":")

        # Count valid hour possibilities
        if hours == "??":
            count_hours = 24
        elif hours[0] == "?":
            count_hours = 3 if hours[1] < "4" else 2  # '0-3' for ?X, '0-1' for ?4-?9
        elif hours[1] == "?":
            count_hours = 10 if hours[0] < "2" else 4  # '0-9' for 0/1X, '0-3' for 2X
        else:
            count_hours = 1  # No '?', so only one possibility

        # Count valid minute possibilities
        if minutes == "??":
            count_minutes = 60
        elif minutes[0] == "?":
            count_minutes = 6  # '?X' -> '0-5'
        elif minutes[1] == "?":
            count_minutes = 10  # 'X?' -> '0-9'
        else:
            count_minutes = 1  # No '?', so only one possibility

        return count_hours * count_minutes
