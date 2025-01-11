class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # new_title = []

        # for word in title.split():
        #     if len(word) < 3:
        #         new_title.append(word.lower())
        #     else:
        #         new_title.append(word[0].upper() + word[1:].lower())

        # return " ".join(new_title)

        # Abridged version using list comprehension
        return " ".join(
            word.lower() if len(word) < 3 else word.capitalize()
            for word in title.split()
        )
