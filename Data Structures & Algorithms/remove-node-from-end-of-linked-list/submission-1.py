# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #remove the nth node from the end of the list
        #create a dummy node and link that with head
        #move fast pointer n+1 steps
        #then move both slow and fast the same speed ( one increment)

        #now slow stops just before the node we want to remove
        #we simply connect slow to slow.next.next
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next



        