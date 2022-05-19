from datetime import datetime
from typing import List


class Solution:
    def containsDuplicate(self, numbers: List[int]) -> bool:
        """
        # O(NLogN)
        numbers.sort()
        for i in range(len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                result = True
                break
        return result
        """
        # O(N)
        map = {}
        i = 1
        for i in range(len(numbers)):
            if numbers[i] in map:
                print([map[numbers[i]], i])
                return True
            map[numbers[i]] = i
        return False


sol = Solution()
print(sol.containsDuplicate([5, 2, 3, 1, 5, 2]))
