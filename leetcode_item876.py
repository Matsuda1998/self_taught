# 提出用
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:# returnもListNodeなのでチェック用ではだめ。
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        m = 1
        measure = head
        current = head
        new_head = ListNode()
        new_current = ListNode()
        while measure.next is not None: # headの要素数を数える
            measure = measure.next
            n += 1
        while current.next is not None and m <= n//2 : # headを直接ループさせない
            current = current.next                     # 頭の位置を残しておく
            m += 1
        new_head = current
        new_current = new_head
        while current.next is not None and new_current.next is not None:
            current = current.next
            new_current = new_current.next
        return new_head # new_currentにすると最後だけリターンされる


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



