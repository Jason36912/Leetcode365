'''
描述：两棵二叉树，叠到一起，相同位置的数进行相加，否则不为NULL的节点直接作为新的子节点
思路：递归，迭代
'''
from typing import *
# difinition for a binary tree node
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def add(self, item):
        """
        param: item 是传进来来的数据,我们要实例化一个结点取接收他,但是他的位置要放在树梢,不能乱插入
                queue 我们创建一个队列来接收和弹出结点,这样我们找到结点需要接收的位置
        """
        node = TreeNode(item)
        if self.val is None:
            """如果根结点是None,是一颗空数,我们就把node赋值给root,那么下面的while循环是不会受影响的,因为是队列[None]的bool值是True"""
            self.val = node
            return
        queue = [self.val]
        while queue:
            """队列的弹出要加0,与栈相仿"""
            cur_node = queue.pop(0)
            if cur_node.left is None:
                """这里有空位,我们插入结点,如果能插入,就完事了"""
                cur_node.left = node
                return
            else:
                """cur_node的左孩子我们放进队列中,下次循环左子结点"""
                queue.append(cur_node.left)

            """同理对右边的操作一样,还是手敲下吧"""

            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)


class Solution:
    def mergeTwoTrees(self, t1:TreeNode, t2:TreeNode):

        # def dfs(t1,t2):
        #     if not (t1 and t2):
        #         return t1 if t1 else t2
        #     # 让t1的值等于二者的累加
        #     t1.val  += t2.val
        #     t1.left = dfs(t1.left,t2.left)
        #     t1.right = dfs(t1.right, t2.right)
        #     return t1
        # return dfs(t1,t2)

        if not (t1 and t2):
            return t1 if t1 else t2
        # 让t1的值等于二者的累加
        t1.val  += t2.val
        t1.left = self.mergeTwoTrees(t1.left,t2.left)
        t1.right = self.mergeTwoTrees(t1.right, t2.right)
        return t1

