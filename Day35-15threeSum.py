'''
描述：包含n个整数1的数组nums，是否存在三个元素相加为0，找出满足所有条件的a,b,c
思路：升序数组+双指针
'''

from typing import *
class Solution():
    def threeSum(self,nums:List[int]):
        n = len(nums)
        nums.sort()
        ans = list()

        for first in range(n):
            # 要和上次的数不一样
            if first > 0 and nums[first] == nums[first-1]:
                continue
             # c 对应的指针指向数组最右端
            third = n - 1
            target = - nums[first]

            #枚举b
            for second in range(first+1, n):
                # 需要和上次枚举的数不一样
                if second > first+1 and nums[second] == nums[second-1]:
                    continue
                # 需要保证b指针在c的左边
                if second < third and nums[second]+nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    ans.append([nums[first],nums[second],nums[third]]) #最外面的方括号
        return ans

nums = [-1,0,1,2,-1,-4]
s = Solution()
a = s.threeSum(nums)
print(a)