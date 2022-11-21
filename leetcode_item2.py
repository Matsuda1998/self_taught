# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        l1_list = []
        current2 = l2
        l2_list = []
        ans_list = []
        ans_element = None

        while current1.next is not None:
            l1_list.append(current1.val)
            current1 = current1.next
        l1_list.append(current1.val)
        while current2.next is not None:
            l2_list.append(current2.val)
            current2 = current2.next
        l2_list.append(current2.val)

        flag = None
        while len(l1_list) or len(l2_list) :
            if len(l1_list) and len(l2_list):
                ans_element = l1_list.pop(0) + l2_list.pop(0)
            elif len(l1_list) :
                ans_element = l1_list.pop(0)
            else :
                ans_element = l2_list.pop(0)
            if flag == 1:
                ans_element += 1
            if ans_element >= 10:
                ans_element -= 10
                flag = 1
            else :
                flag = 0
            ans_list.append(ans_element)
        if flag == 1 :
            ans_list.append(1)
       
        answer = ListNode(ans_list.pop(0))
        current_ans = answer
        while ans_list :
            current_ans.next = ListNode(ans_list.pop(0))
            current_ans = current_ans.next
        return answer
            


