class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        key_set = []
        for c in key:
            if c not in key_set:
                key_set.append(c)
        key = "".join(key_set)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        decoded = []

        for c in message:
            if c == " ":
                decoded.append(c)
            else:
                idx = key.index(c)
                decoded.append(alphabet[idx])

        return "".join(decoded)
