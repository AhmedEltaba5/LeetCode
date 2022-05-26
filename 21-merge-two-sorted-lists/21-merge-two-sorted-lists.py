# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        res = dummy = ListNode()
        
        while list1 and list2:
            if list1.val>list2.val:
                dummy.next = ListNode(list2.val)
                dummy = dummy.next
                list2 = list2.next
            else:
                dummy.next = ListNode(list1.val)
                dummy = dummy.next
                list1 = list1.next
        while list1:
            dummy.next = ListNode(list1.val)
            dummy = dummy.next
            list1 = list1.next
        while list2:
            dummy.next = ListNode(list2.val)
            dummy = dummy.next
            list2 = list2.next
        return res.next
        