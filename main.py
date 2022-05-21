import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t1 = t2 = 0
        nums1.sort()
        nums2.sort()
        result = []
        while (t1 < len(nums1)) and (t2 < len(nums2)):
            if nums1[t1] == nums2[t2]:
                result.append(nums1[t1])
                t1 += 1
                t2 += 1
            elif nums1[t1] > nums2[t2]:
                t2 += 1
            else:
                t1 += 1
        return result

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)
        nums2.sort()

        def binarySearch(number: int, numberList: List[int]):
            left, right = 0, len(numberList)-1
            while left <= right:
                mid = left + (right - left) // 2
                if numberList[mid] == number:
                    return True
                if numberList[mid] > number:
                    right = mid-1
                else:
                    left = mid+1
            return False

        result = set()
        for i in nums1:
            if binarySearch(i, nums2):
                result.add(i)
        return list(result)


sol = Solution()
ans = sol.intersection(
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
)
print(ans)
