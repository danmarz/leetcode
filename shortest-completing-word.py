class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Initialize an empty string to store the characters from licensePlate
        arr = ""

        # Sort the words array based on their lengths
        words = sorted(words, key=len)

        # Iterate through each character in licensePlate
        for i in licensePlate:
            # Check if the character is an alphabetic character
            if i.isalpha():
                # If yes, append its lowercase version to arr
                arr += i.lower()

        # Iterate through each word in the sorted words array
        for w in words:
            # Iterate through each character in arr
            for i in range(len(arr)):
                # Get the current character from arr
                s = arr[i]
                # Check if the count of s in the word is less than the count of s in arr
                if w.count(s) < arr.count(s):
                    # If so, break out of the loop and move to the next word
                    break
                # If we've checked all characters in arr and found no discrepancies
                if i == len(arr) - 1:
                    # Return the current word as the shortest completing word
                    return w
