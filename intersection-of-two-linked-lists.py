# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        # calculate the lengths of both lists using the getLength function above.
        lenA = getLength(headA)
        lenB = getLength(headB)

        diff = abs(lenA - lenB)
        if lenA > lenB:
            longer = headA
            shorter = headB
        else:
            longer = headB
            shorter = headA

        # move forward the longer pointer by the difference in lengths.
        for _ in range(diff):
            longer = longer.next

        # iterate simultaneously both pointers until they meet at an intersection point (if it exists).
        while longer and shorter:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next

        # if no intersection is found, then return None.
        return None
