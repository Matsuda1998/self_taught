from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort(key = len)
        if len(strs) == 1:
            return strs[0]
        if len(strs[0]) == 0:
            return ""
        for j in range(len(strs[0])):
            compare = strs[0][j]
            for i in range(1,len(strs)):
                if compare != strs[i][j]:
                    break
            else :
                ans += compare
                continue
            break
        return ans

strs=["flower",
      "flow",
      "flight"]
strs[0][0]
strs.sort(key = len)
strs
s=""
len(s)