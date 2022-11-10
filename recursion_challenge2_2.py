# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""leetcodeのサイトでListNodeを入れるコンテナをどう実装しているか
不明だが下記コードでＯＫがでた。サンプルの[1,2,2,1]の各要素がListNode,
それのコンテナもリストノード？
class Solution:
    def isPalindrome(self, head:Optional[ListNode]) -> bool:
        l=[]
        while head is not None:
            l.append(head.val)
            head = head.next
        reverse_l=l[::-1]
        return l == reverse_l
"""
"""自分が実装したコンテナ(Linkedlist)でSolutionクラスを書き直すと
以下となる。"""
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        current=self.head
        if current is None:
            print("empty linkedlist")
        while current is not None:
            print(current.val,end=" ")
            current=current.next
    def append(self,new_node:ListNode):
        if self.head is None:
            self.head = new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node
        return
    def pop(self):
        if self.head is None:
            #print("IndexError: pop from empty linkedlist")
            return
        current=self.head
        previous=None
        while current.next is not None:
            previous=current
            current=current.next
        if previous is None:#元の要素が一つしかない場合
            self.head = None
        else:
            previous.next=None#元の要素が二つ以上の場合
        temp=current
        del current
        return temp

class Solution:
    def isPalindrome(self, head:Optional[Linkedlist]) -> bool:
        l=[]
        while head.head is not None:
            l.append(head.head.val)
            head.head = head.head.next
        reverse_l=l[::-1]
        return l == reverse_l

linkedlist1=Linkedlist()
linkedlist1.printlist()
linkedlist1.append(ListNode(1))
linkedlist1.append(ListNode(1))
linkedlist1.append(ListNode(2))
linkedlist1.append(ListNode(2))
linkedlist1.append(ListNode(1))
a=Solution()
a.isPalindrome(linkedlist1)


"""解答のListNodeクラスにコンテナ化するメソッドを書いてみる
これができれば１００％
できた！恐らくleetcodeのなかのListNodeクラスはこうなっている筈！"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def append(self,new_node):#new_nodeにアノテーションでデータ型指定(:Listnode)
                              #するとnameErrorでるのでこれをあきらめる
                              #恐らくListNodeのクラス定義が終わってないのに使った為
        if self is None:
            self=new_node
            return
        current=self
        while current.next is not None:
            current=current.next
        current.next=new_node
        return

class Solution:
    def isPalindrome(self, head:Optional[ListNode]) -> bool:
        l=[]
        while head is not None:
            l.append(head.val)
            head = head.next
        reverse_l=l[::-1]
        return l == reverse_l

my_listnode=ListNode(1)
my_listnode.append(ListNode(2))
my_listnode.append(ListNode(2))
my_listnode.append(ListNode(1))

Solution().isPalindrome(my_listnode)
