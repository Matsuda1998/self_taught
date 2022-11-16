# 提出用
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:# returnもListNodeなのでチェック用ではだめ。
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        while head.next is not None:
            head = head.next
            n += 1
        m = 1
        current = head
        while m <= (n // 2) and current.next is not None :
            temp = current
            current = current.next
            m += 1
            del temp
        return current

            





# チェック用
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def append(self,new_node):#new_node:Listnode
        if self is None:
            self=new_node
            return
        current=self
        while current.next is not None:
            current=current.next
        current.next=new_node
        return
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list=[]
        while head is not None:
            head_list.append(head.val)
            head = head.next
        n=len(head_list)
        return head_list[n // 2 :]
head=ListNode(1)
head.append(ListNode(2))
head.append(ListNode(3))
head.append(ListNode(4))
head.append(ListNode(5))

Solution().middleNode(head)



