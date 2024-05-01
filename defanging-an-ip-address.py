class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Replace "." with "[.]" using the replace method
        return address.replace(".", "[.]")
