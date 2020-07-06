''''
描述：包含整数的有序数组，每个元素出现两次，只有一个出现一次，找出它
思路：二分法；
    仅对偶数数组进行二分索引；
'''
from typing import *
class Solution(object):
    def singleNonDuplicate1(self,nums:List[int]):
        lo = 0
        hi = len(nums)-1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            halves_even = (hi - mid) %2 == 0
            if nums[mid+1] == nums[mid]:
                if halves_even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid-1] == nums[mid]:
                if halves_even:
                    hi = mid - 2
                else:
                    lo = mid + 1

            else:
                return nums[mid]
        return nums[lo]

nums = [1,1,4,4,5,5,6,6,8,9,9]
s = Solution()
a = s.singleNonDuplicate1(nums)
print(a)