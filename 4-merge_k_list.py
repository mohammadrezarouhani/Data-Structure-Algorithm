# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []


# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            
        prev, cur, head = None, None, None

        for pointer in lists:
            if not head:
                head = pointer
                new_pointer = head

                while pointer:
                    pointer = pointer.next
                    new_pointer.next = pointer
                    new_pointer = new_pointer.next
            else:
                prev = None
                cur = head

                while pointer:
                    if not cur:
                        new_node = ListNode(pointer.val)
                        prev.next = new_node
                        prev=new_node
                        pointer=pointer.next

                    elif pointer.val < cur.val and cur:
                        new_node = ListNode(pointer.val, cur)

                        if prev:
                            prev.next = new_node
                        else:
                            head = new_node

                        prev = new_node
                        pointer = pointer.next

                    else:
                        prev = cur
                        cur = cur.next

        return head



head = None
node = None
lists = []

for li in [[1,2,3],[-1]]:
    for val in li:
        if node:
            node.next = ListNode(val)
            node = node.next
        else:
            node = ListNode(val)
            head = node

    lists.append(head)
    node = None

# for pointer in lists:
#     while pointer:
#         print(pointer.val)
#         pointer=pointer.next

s = Solution()
res = s.mergeKLists(lists)


while res:
    print(res.val)
    res = res.next
    





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




# time optimized
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize a min heap
        heap = []
        heapq.heapify(heap)
        
        # Add the first element from each list to the heap along with its list index
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            # Pop the smallest element from the heap
            val, list_idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # If there are more elements in the list, add the next element to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
        return dummy.next