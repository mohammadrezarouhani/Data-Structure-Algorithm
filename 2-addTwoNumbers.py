import pdb
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        start=self
        li=[]
        while(start):
            li.append(start.val)
            start=start.next
        return str(li)
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum=l1.val+l2.val
        result=sum % 10
        carry=sum//10

        start=ListNode(result)
        tail=start

        l1=l1.next
        l2=l2.next

        while(1):
            if l1==None and l2==None:
                break
            elif l1==None:
                sum=l2.val+carry
                result=sum % 10
                carry=sum//10
                l2=l2.next
            elif l2==None:
                sum=l1.val+carry
                result=sum % 10
                carry=sum//10
                l1=l1.next
            else:
                sum=l1.val+l2.val+carry
                result=sum%10
                carry=sum//10
                l1=l1.next
                l2=l2.next

            print(result)
            tail.next=ListNode(result)
            tail=tail.next

        return start


l1=ListNode(9)
l1_tail=l1

l2=ListNode(9)
l2_tail=l2

for val in [9,9,9,9,9,9]:
    l1_tail.next=ListNode(val)
    l1_tail=l1_tail.next


for val in [9,9,9,9]:
    l2_tail.next=ListNode(val)
    l2_tail=l2_tail.next


s=Solution()
s.addTwoNumbers(l1,l2)