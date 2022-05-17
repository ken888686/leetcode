from typing import Optional
from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next: ListNode = None):
        self.val = val
        self.next = next


class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            currentChar = s[i]
            if currentChar in usedChar and start <= usedChar[currentChar]:
                start = usedChar[currentChar] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[currentChar] = i
        return maxLength

    def logN(self):
        Numbers = [5, 17, 33, 41, 55, 61]
        Find = 55
        low = 0
        high = len(Numbers) - 1
        while low <= high:
            mid = (low + high) // 2
            if Numbers[mid] > Find:
                high = mid - 1
            elif Numbers[mid] < Find:
                low = mid + 1
            else:
                break
        print(Numbers[mid])

    def reverseStr(self, inputStr):
        result = ''
        for index in reversed(range(len(inputStr))):
            result += inputStr[index]
        return result

    def palindromeStr(self, inputStr):
        return inputStr == inputStr[::-1]

    def mostChar(self, inputStr):
        strList = {}
        maxCount = 0
        for i in range(len(inputStr)):
            currentChar = inputStr[i]
            strList[currentChar] = strList[currentChar] + \
                1 if currentChar in strList else 1
            maxCount = max(maxCount, strList[currentChar])
        return maxCount

    def fizzBuzz(self, inputNum):
        result = ''
        for i in range(1, inputNum+1):
            temp = ''
            if i % 3 == 0:
                temp += 'Fizz'
            if i % 5 == 0:
                temp += 'Buzz'
            result += "{} ".format(i if temp == "" else temp)
        return result

    def arrayChuck(self, arr: list[int], n: int) -> list[int] | list[list[int]]:
        result: list[int] | list[list[int]] = []
        temp: list[int] = []
        for i in range(0, len(arr), n):
            temp = arr[i:i+n]
            if len(temp) < n:
                for j in temp:
                    result.append(j)
            else:
                result.append(temp)
        return result

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return head.next


sol = Solution()
list1 = ListNode(2, ListNode(4, ListNode(6)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
result = sol.mergeTwoLists(list1, list2)
print(result)
