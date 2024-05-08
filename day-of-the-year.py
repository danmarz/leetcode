from datetime import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split("-"))
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)):
            days_in_month[2] = 29

        return d + sum(days_in_month[:m])

        """
        # Parse the input date string into a datetime object
        dt = datetime.strptime(date, '%Y-%m-%d')
        # Get the day number of the year
        day_number = dt.timetuple().tm_yday
        return day_number
        """

        """
        monthDays = [31,30] * 3
        monthDays[1] = 28
        
        monthDays = monthDays + [31,31,30,31,30,31]

        year, month, day = date.split("-")

        if int(year) % 100 == 0 and int(year) % 400 == 0:
            monthDays[1] = 29
        elif int(year) % 4 == 0 and int(year) % 100 != 0:
                monthDays[1] = 29
    
        ans = 0

        if int(month) > 1:
            for i in range(int(month) - 1):
                ans += monthDays[i]
        
        ans += int(day)
        
        return ans
        """
