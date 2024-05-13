import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        # Create a datetime object for the given date
        date_object = datetime.date(year, month, day)

        # Get the day of the week as an integer (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
        day_of_week_int = date_object.weekday()

        # Map the integer representation of the day to the corresponding string
        days_of_week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        day_of_week_str = days_of_week[day_of_week_int]

        return day_of_week_str

        """
        # Zeller's Congruence algorithm
        if month < 3:
            month += 12
            year -= 1
        
        century = year // 100
        year_of_century = year % 100
        
        day_of_week = (day + ((13 * (month + 1)) // 5) + year_of_century + (year_of_century // 4) + (century // 4) - (2 * century)) % 7
        
        # Map the result to the corresponding day of the week
        days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days_of_week[day_of_week] 
        """
