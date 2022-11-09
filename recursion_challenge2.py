#https://leetcode.com/problems/palindrome-linked-list/
"""linked listは'連結リスト'のことであり
listではない！理解するの面倒だし、取り敢えず
recursionの練習なのでリストとしてやる"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from email import header


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse_head=head[::-1]
        return head == reverse_head
a=[1,1,1,1,1,1]
b=Solution()
b.isPalindrome(a)
#再帰的にやってみる
class Solution:
    def __init__(self,head):
        self.head=head
        self.copy_head=head[:]
        self.reverse_head=[]

    def isPalindrome(self):
        if len(self.copy_head) == 0:
            return self.head == self.reverse_head
        self.reverse_head.append(self.copy_head.pop())
        return self.isPalindrome()

a=Solution([1,2,1])
a.isPalindrome()

#↓linkedlist を理解しながらやってみる。
#https://www.delftstack.com/ja/howto/python/linked-list-in-python/
#上記サイトが連結リストの説明が一番わかりやすい
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None#初期値。最初のノードをいれるためにある
    def printlist(self):
        current=self.head
        if current is None:
            print("empty linkedlist")
        while current is not None:
            print(current.data,end=" ")
            current=current.next
    def append(self,new_node:Node):
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
            #エラーを吐くコードを入れるIndexError: pop from empty linkedlist
            #か自分で書く
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
        





mynode1=Node(10)            #手書きでlinkedlistを作ってみる
mynode2=Node(20)            #ノードを4つ作り
mynode3=Node(30)            #next変数に次のノードを代入(=参照=ポインタ)
mynode4=Node(40)            #頭の中だけで考えるよりこうやって書いてみると
mylinkedlist=Linkedlist()   #わかりやすい！
mylinkedlist.head=mynode1   #
mynode1.next=mynode2        #
mynode2.next=mynode3        #
mynode3.next=mynode4        #ここまで

mylinkedlist.printlist()
print(mylinkedlist.head,mylinkedlist.head.next,mylinkedlist.head.next.next,mylinkedlist.head.next.next.next,mylinkedlist.head.next.next.next.next)
mylinkedlist2=Linkedlist()
mylinkedlist2.append(Node(1))
mylinkedlist2.append(Node(2))
mylinkedlist2.append(Node(2))
mylinkedlist2.append(Node(1))
mylinkedlist2.printlist()
last=mylinkedlist2.pop()
mylinkedlist2.printlist()
print(last.data)



#ここから提出用
#出来たけどleetcodeへ回答を送るとlist何たらと怒られる。
#これはこれでよいので別ファイルでもう一度考える
    
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution(Linkedlist):
    def makelinkedlist(self,l:list):
        fwd_ll=Linkedlist()
        for i in l:
            fwd_ll.append(ListNode(i))
        return fwd_ll
    def reverselinkedlist(self,l:list):
        fwd_ll=self.makelinkedlist(l)
        rvs_ll=Linkedlist()
        while fwd_ll.head is not None:
            rvs_ll.append(fwd_ll.pop())
        return rvs_ll
    def isPalindrome(self, l:list):
        fwd=self.makelinkedlist(l)
        rvs=self.reverselinkedlist(l)
        f_current=fwd.head
        r_current=rvs.head
        while f_current.next is not None and r_current.next is not None:
            if f_current.val != r_current.val:
                return False
            f_current=f_current.next
            r_current=r_current.next
        if f_current.val != r_current.val:
            return False
        return True
a=Solution()
a.isPalindrome([1,2,2,1])