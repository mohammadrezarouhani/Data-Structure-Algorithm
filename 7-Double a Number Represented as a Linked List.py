# Definition for singly-linked list.
import pdb


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num = 0
        pointer = head

        while pointer:
            num *= 10
            num += pointer.val
            pointer = pointer.next
        else:
            num *= 2
            head = None

        if num == 0:
            head = ListNode(0)
        else:
            while num:
                val = num % 10
                num //= 10
                new_node = ListNode(val, head)
                head = new_node

        return head


# node3 = ListNode(9)
# node2 = ListNode(8, node3)
node1 = ListNode(0)

s = Solution()

res = s.doubleIt(node1)


while res:
    print(res.val)
    res = res.next
