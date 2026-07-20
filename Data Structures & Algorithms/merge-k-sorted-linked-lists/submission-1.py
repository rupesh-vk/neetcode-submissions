# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #merge k sorted lists into a single 

        #we implement merge two lists, many times.
        if not lists:
            return None

        def merge2Lists(list1: List[Optional[ListNode]], list2:List[Optional[ListNode]]):
            
            dummy = ListNode()
            curr = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            curr.next = list1 or list2
            return dummy.next
        
        # Keep merging pairs until only one list remains
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]

                if i+1 < len(lists):
                    list2 = lists[i+1]
                else:
                    list2 = None
                mergedLists.append(merge2Lists(list1, list2))
            lists = mergedLists
        return lists[0]

            


        