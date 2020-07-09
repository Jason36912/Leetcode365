'''
描述：打印链表中的倒数第k个节点
思路：链表相关的知识点：递归，反转，双指针，环
    出现“倒数”，用双指针

'''
#from typing import *
class ListNode:
    def __init__(self,data,next =None):
        self.val = data
        self.next = next

class Solution:
    def getKthFromEnd(self,head:ListNode,k:int):
        former, latter = head,head
                                    #考虑特殊情况，head为空指针或者k=0
                                    # 考虑特殊情况，k大于列表的长度
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next,latter.next
        return latter

node1 = None
node2 = ListNode(1,None)
node3 = ListNode(2,node2)
node4 = ListNode(3,node3)
node5 = ListNode(4,node4)

#print(node1,node2.val,node3,node4.next)

s =Solution()
v  = s.getKthFromEnd(node2,2)
print(v.val)
