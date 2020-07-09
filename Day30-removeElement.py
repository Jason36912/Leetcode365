'''
描述：给定数组num和一个值val, 原地删除数组中所有等于val的数，
      返回移除后数组的新长度
      要求，不使用额外空间，不需要考虑数组中超出新长度后面的元素
'''

class Solution():
    def removeElement(self,nums,val):
        res = 0
        for num in nums:
            if (num != val):
                nums[res] = num
                res += 1
        return res

nums = [2,3,2,2,3,2]
val = 3
s = Solution()
length = s.removeElement(nums,val)
print(length)