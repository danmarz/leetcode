class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiou"
        finalSentence = ""

        for pos, word in enumerate(sentence.split()):
            numA = ""
            for _ in range(pos + 1):
                numA += "a"

            if word[0].lower() in vowels:
                finalSentence = word + "ma" + numA + " " + finalSentence
            else:
                finalSentence = word[1:] + word[0] + "ma" + numA + " " + finalSentence

        return " ".join(reversed(finalSentence.split()))

        # pythonic way
        """
        vowels = list('aeiou')
        words = sentence.split(' ')
        new_words =  [word + 'ma' if word[0].lower() in vowels else word[1:]+word[0]+'ma' for word in words] 
        final_words = [new_words[i] + 'a' *(i+1) for i in range(len(new_words))]
        
        return ' '.join(final_words)
        """
