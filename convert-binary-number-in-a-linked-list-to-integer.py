# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # build the answer directly using left shift & bitwise OR
        num = 0
        while head:
            num = (num << 1) | head.val
            head = head.next
        return num

        # build the binary representation of the answer using a string
        """
        binaryString = ""

        while head:
            binaryString += str(head.val)
            if head.next:
                head = head.next
            else:
                break

        return int(binaryString, 2)
        """
