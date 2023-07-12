# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        new_node= ListNode(0)
        curr = new_node
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            added = carry + x + y
            carry = added // 10
            curr.next = ListNode(added % 10)

            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 =l2.next


        if carry > 0:
            curr.next = ListNode(carry)
        
        return new_node.next
    