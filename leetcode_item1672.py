from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        checklist = []
        for val in accounts:
            n = 0
            for j in val :
                n += j
            checklist.append(n)
        checklist.sort(reverse = 1)
        return checklist[0]

Solution().maximumWealth([[1,5],[7,3],[3,5]])

