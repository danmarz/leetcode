# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

    # short version
    """
        ans = head
        while ans:
            while ans.next and ans.next.val == ans.val:
                ans.next = ans.next.next
            ans = ans.next
        return head
    """
