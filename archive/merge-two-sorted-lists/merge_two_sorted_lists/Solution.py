class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        ptr = list1
        if list1.val > list2.val:
            ptr = list2
            list2 = list2.next
        else:
            list1 = list1.next
        curr = ptr
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if not list1:
            curr.next = list2
        else:
            curr.next = list1
        
        return ptr