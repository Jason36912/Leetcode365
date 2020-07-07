'''
描述：两个有序数组，合并到一起。可以假设nums1有足够空间
方法：合并后排序；
        双指针从前往后；
        双指针从后往前。
'''
class Solution(object):
    def merge(self,nums1,m,nums2,n):
        '''
        :param nums1: List
        :param m: int
        :param nums2: List
        :param n: int
        :return:
        '''
        p1 = m - 1
        p2 = n - 1
        p = m+n-1

        while p1>=0 and p2>=0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        # add missing elements from nums2
        nums1[:p2+1] = nums2[:p2+1]

        return nums1

nums1 = [1,2,3,0,0,0]
#nums1 = [1,2,3,0,0,0,0]
nums2 = [2,5,6]

s = Solution()
num = s.merge(nums1,3,nums2,3)
print(num)