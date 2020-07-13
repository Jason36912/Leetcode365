'''
18描述：给定单项目链表的头结点和删除的的值，定义一个函数删该值
思路：删除的是头结点，直接返回head.next
'''''


from typing import *
class ListNode:
    def __init__(self,data,next =None):
        self.val = data
        self.next = next
class Solution:
    def deleteNode(self,head:ListNode,val:int):
        if (head.val == val):
            return head.next
        pre, cur = head,head.next
        if (cur.val & cur.val != val):
            pre = cur
            cur = cur.next
        return head
node1 = None
node2 = ListNode(1,None)
node3 = ListNode(2,node2)
node4 = ListNode(3,node3)
node5 = ListNode(4,node4)

#print(node1,node2.val,node3,node4.next)

s =Solution()
v  = s.deleteNode(node5,4)
print(v.val)
