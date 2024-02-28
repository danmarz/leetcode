class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Define the Morse code representation for each letter
        morse_code = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        # Create a set to store unique Morse code transformations
        unique_transformations = set()

        # Iterate over each word in the input list
        for word in words:
            # Initialize an empty string to store the Morse code transformation of the current word
            transformation = ""
            # Iterate over each character in the word
            for char in word:
                # Get the index of the character in the alphabet (a=0, b=1, c=2, ..., z=25)
                index = ord(char) - ord("a")
                # Append the Morse code representation of the character to the transformation string
                transformation += morse_code[index]
            # Add the transformation to the set
            unique_transformations.add(transformation)

        # Return the number of unique transformations
        return len(unique_transformations)
