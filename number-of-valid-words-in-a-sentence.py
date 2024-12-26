class Solution:
    def countValidWords(self, sentence: str) -> int:
        punctuations = {"!", ".", ","}
        tokens = sentence.split()
        valid_word_count = 0

        for token in tokens:
            if any(char.isdigit() for char in token):
                continue  # Skip if the token contains digits

            hyphen_count = token.count("-")
            if hyphen_count > 1:
                continue  # More than one hyphen is invalid

            if hyphen_count == 1:
                hyphen_index = token.index("-")
                # Ensure the hyphen is surrounded by lowercase letters
                if (
                    hyphen_index == 0
                    or hyphen_index == len(token) - 1
                    or not (
                        token[hyphen_index - 1].islower()
                        and token[hyphen_index + 1].islower()
                    )
                ):
                    continue

            punctuation_count = sum(1 for char in token if char in punctuations)
            if punctuation_count > 1:
                continue  # More than one punctuation is invalid

            if punctuation_count == 1 and token[-1] not in punctuations:
                continue  # Punctuation must be at the end of the token

            if any(char in punctuations for char in token[:-1]):
                continue  # Punctuation in the middle of the token is invalid

            valid_word_count += 1  # Increment count if all checks pass

        return valid_word_count
