'''
描述：两个非空链表代表两个非空整数，数字最高位位于链表的开始位置。它们每个节点只存储一个数字，
     将这两个数相加得到一个新的链表。
     可以假设除数字0外，这两个数字都不会以0开头
进阶，链表不能翻转怎么处理
思路：最右边数字对齐，用栈来存放链表的每个值，
      相加产生进位，用flag表示是否有进位。

'''
from pythonds.basic.stack import Stack
from typing import *

class ListNode:
    def __init__(self,data,next =None):
        self.val = data
        self.next = next
class LinkList(object):
    def __init__(self):
        self.head = None
    #链表初始化函数, 方法类似于尾插
    def initList(self, data):
        #创建头结点
        self.head = ListNode(data[0])
        p = self.head
        #逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next


class Solution:
    def addTwoNumbers(self,v1:ListNode,v2:ListNode):
        s1, s2 = [], []
        while v1:
            s1.append(v1.val)
            v1 = v1.next
        while v2:
            s2.append(v2.val)
            v2 = v2.next
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans

data1 = [7,2,4,3]
data2 = [5,6,4]

l1 = LinkList()
l2 = LinkList()
l1.initList(data1)
l2.initList(data2)

s = Solution()

result = s.addTwoNumbers(l1.head,l2.head)
while result:
    print(result.val)
    result =result.next