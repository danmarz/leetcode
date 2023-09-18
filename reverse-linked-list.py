# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initialize the previous node as None
        current = head  # Initialize the current node as the head

        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the next pointer of the current node
            prev = current  # Move the previous pointer forward
            current = next_node  # Move the current pointer forward

        return prev  # Return the new head (which is the previous node)
