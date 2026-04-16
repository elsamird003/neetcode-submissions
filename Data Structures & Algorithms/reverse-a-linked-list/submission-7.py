# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # IN A SLIGHLY LIKED LIST THE TAIL ALAWYS POINTS TO NONE 
        curr = head

        while curr:
            temp = curr.next # save the rest of the linked list
            curr.next = prev # REVERSE THE LINKED LIST TO POINTS (BACKWARDS)
            prev = curr # Points prev to points foward
            curr = temp
        return prev


