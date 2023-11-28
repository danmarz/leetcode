class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

        result = []
        for word in words:
            # Convert each word's characters to lowercase for comparison
            word_lower = word.lower()

            # Check if all characters of the word are present in any of the keyboard rows
            for row in keyboard_rows:
                if all(ch in row for ch in word_lower):
                    result.append(word)
                    break

        return result
