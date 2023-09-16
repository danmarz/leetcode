# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to serve as the new head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy  # Initialize a pointer to the dummy node

        # Traverse the list
        while head:
            if head.val == val:
                # If the current node has the target value, skip it
                prev.next = head.next
            else:
                # Move the previous pointer forward
                prev = head
            head = head.next

        return dummy.next  # Return the real head (after the dummy)
