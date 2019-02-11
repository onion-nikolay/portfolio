# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        def createNode(l1: 'ListNode', l2: 'ListNode', start=0):
            val1 = 0 if type(l1) is not 'ListNode' else l1.val
            val2 = 0 if type(l2) is not 'ListNode' else l2.val
            _sum = val1 + val2 + start
            if _sum == 0:
                return
            l3 = ListNode(_sum % 10)
            l3.next = createNode(l1.next, l2.next, _sum // 10)
            return l3

        return createNode(self, l1, l2)

l1 = ListNode(2)
