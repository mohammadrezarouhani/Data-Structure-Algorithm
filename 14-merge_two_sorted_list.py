from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1, l2 = list1, list2

        if l1 and l2:
            if l1.val > l2.val:
                new_list = ListNode(l2.val)
                l2 = l2.next
            else:
                new_list = ListNode(l1.val)
                l1 = l1.next

            head = new_list
        elif l1:
            new_list = ListNode(l1.val)
            l1=l1.next
        elif l2:
            new_list = ListNode(l2.val)
            l2=l2.next
        else:
            new_list = None

        head=new_list
        while l1 and l2:
            if l1.val > l2.val:
                new_list.next = ListNode(l2.val)
                l2 = l2.next
            else:
                new_list.next = ListNode(l1.val)
                l1 = l1.next

            new_list = new_list.next

        while l1:
            new_list.next = ListNode(l1.val)
            new_list = new_list.next
            l1 = l1.next

        while l2:
            new_list.next = ListNode(l2.val)
            new_list = new_list.next
            l2 = l2.next

        return head


def create_linked_list(arr: list):
    if arr:
        head = ListNode(arr[0])
        pointer = head
        for a in arr[1:]:
            pointer.next = ListNode(a)
            pointer = pointer.next
    else:
        head = None

    return head


def print_linked_list(l: ListNode):
    while l:
        print(l.val)
        l = l.next


s = Solution()
list1 = create_linked_list([0,1,2,3,4,5,6])
list2 = create_linked_list([])
res = s.mergeTwoLists(list1, list2)

print_linked_list(res)
