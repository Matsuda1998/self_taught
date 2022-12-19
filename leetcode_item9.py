"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str =str(x)
        if x_str == x_str[::-1]:
            return True
        else:
            return False
"""
# 文字列に返還しないでやってみる(フォローアップで言われた)
# 出来たけど全然おせぇ。無駄な計算多いかも。
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        if 0 <= x and x < 10:
            return True
        i = 0
        while x // 10**i >= 10 :
            i += 1
        chk_list =[]
        while i >= 0 :
            chk_list.append(x // 10**i)
            x = x % 10**i
            i -= 1
        j = len(chk_list)-1
        m = j //2
        k = 0
        while j > m:
            if chk_list[k] == chk_list[j]:
                j -= 1
                k += 1
            else:
                return False        
        return True

Solution().isPalindrome(20)