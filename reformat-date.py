class Solution:
    def reformatDate(self, date: str) -> str:
        # Split the input string into its components: Day, Month, and Year
        day_str, month_str, year_str = date.split()

        # Create a dictionary to map month abbreviations to their corresponding numbers
        month_mapping = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }

        # Remove the suffix ('st', 'nd', 'rd', 'th') from the day string to extract the day number
        day_num = "".join(filter(str.isdigit, day_str))

        # Ensure the day is in two digits (e.g., '3' becomes '03')
        day_num = day_num.zfill(2)

        # Get the month number from the dictionary
        month_num = month_mapping[month_str]

        # Combine the year, month, and day into the desired format
        formatted_date = f"{year_str}-{month_num}-{day_num}"

        return formatted_date

        # dayString, monthString, year = date.split()
        # day = ""
        # month = 0

        # for char in dayString:
        #     if char.isnumeric():
        #         day += char

        # month_mapping = {month: index for index, month in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1)}
        # month = str(month_mapping.get(monthString, "Invalid month name"))

        # if len(day) == 1:
        #     day = "0" + day

        # if len(month) == 1:
        #     month = "0" + month

        # result = '-'.join(map(str, [year, month, day]))

        # return result
