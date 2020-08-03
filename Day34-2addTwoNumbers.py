''''
描述：两个非空列表，它们各自位数暗中逆序方式存储，每个节点只能存一位，
    将两个数字加起来，返回一个新的列表
私聊：设立一个表示进位的变量carry
'''

class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution():
    def addTwoNumber(self,l1:ListNode,l2:ListNode):
        dummy = pre = ListNode(0)
        carry = 0
        while (l1 != None or l2 != None or carry):
            carry += (l1.val if l1 else 0)+(l2.val if l2 else 0)
            pre.next = ListNode(carry%10)
            pre = pre.next
            carry //=  10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

