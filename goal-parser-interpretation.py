class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")

        # Alternative, more verbose but faster solution below:

        # By using a list and appending to it, and then using ''.join(list) at the end (instead of declaring ans as an empty string) we avoid repeated string concatenation, which is less efficient in Python.

        # ans = []
        # index = 0

        # while index < len(command):
        #     if command[index] == 'G':
        #         ans.append('G')
        #         index += 1
        #     elif command[index:index + 2] == '()':
        #         ans.append('o')
        #         index += 2
        #     elif command[index:index + 4] == '(al)':
        #         ans.append('al')
        #         index += 4

        # return "".join(ans)
