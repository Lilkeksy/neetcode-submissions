# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            # Access the value
            print(curr.val)
            # Move to the next node

            # To avoid losing the rest of the list,
            # save the next node before changing the link
            temp_next = curr.next
            curr.next = prev # Reversing the link
            # Now move forward using the saved reference
            prev = curr
            curr = temp_next
        return prev