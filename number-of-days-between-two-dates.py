# from datetime import datetime

# class Solution:
#     def daysBetweenDates(self, date1: str, date2: str) -> int:
#         # Convert the date strings to datetime objects
#         date_format = "%Y-%m-%d"
#         d1 = datetime.strptime(date1, date_format)
#         d2 = datetime.strptime(date2, date_format)

#         # Calculate the difference between the two dates
#         delta = abs((d2 - d1).days)

#         return delta


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        def is_leap_year(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def days_in_month(year, month):
            if month in [1, 3, 5, 7, 8, 10, 12]:
                return 31
            elif month in [4, 6, 9, 11]:
                return 30
            elif month == 2:
                return 29 if is_leap_year(year) else 28
            return 0

        def days_since_epoch(year, month, day):
            days = 0
            for y in range(1970, year):
                days += 366 if is_leap_year(y) else 365
            for m in range(1, month):
                days += days_in_month(year, m)
            days += day
            return days

        year1, month1, day1 = map(int, date1.split("-"))
        year2, month2, day2 = map(int, date2.split("-"))

        days1 = days_since_epoch(year1, month1, day1)
        days2 = days_since_epoch(year2, month2, day2)

        return abs(days2 - days1)
