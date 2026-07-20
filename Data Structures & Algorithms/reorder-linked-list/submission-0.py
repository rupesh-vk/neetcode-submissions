# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        # divide the list into halves

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        first = head
        # reverse the second half 
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev

        dummy = ListNode()
        current = dummy
        # merge alternatively
        while second:
            current.next = first
            first = first.next
            current = current.next
             
            current.next = second
            second = second.next
            current = current.next
        current.next = first or second

            



        