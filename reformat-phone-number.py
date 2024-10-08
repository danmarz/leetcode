class Solution:
    def reformatNumber(self, number: str) -> str:
        ans = ""
        formattedNumber = number.replace(" ", "").replace("-", "")

        while formattedNumber:
            if len(formattedNumber) == 4:
                ans += formattedNumber[:2] + "-" + formattedNumber[2:4]
                formattedNumber = ""
            elif len(formattedNumber) == 3:
                ans += formattedNumber[:3]
                formattedNumber = ""
            elif len(formattedNumber) == 2:
                ans += formattedNumber[:2]
                formattedNumber = ""
            else:
                ans += formattedNumber[:3] + "-"
                formattedNumber = formattedNumber[3:]

        return ans

        # # List (index-based) approach
        # # Remove all spaces and dashes in one step
        # number = number.replace(' ', '').replace('-', '')

        # # Collect groups in a list
        # blocks = []

        # # Process all but the last few digits
        # i = 0
        # while len(number) - i > 4:
        #     blocks.append(number[i:i+3])
        #     i += 3

        # # Handle the remaining digits
        # if len(number) - i == 4:
        #     blocks.append(number[i:i+2])
        #     blocks.append(number[i+2:i+4])
        # else:
        #     blocks.append(number[i:])

        # # Join all blocks with dashes
        # return '-'.join(blocks)
