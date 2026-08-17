# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        
        if stack:
            newHead = stack.pop()
            cur = newHead
            while stack:
                cur.next = stack.pop()
                cur = cur.next
            cur.next = None
        else:
            return head

        return newHead
        