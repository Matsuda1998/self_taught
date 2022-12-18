class Solution:
    def myAtoi(self, s: str) -> int:
        ans_str=""
        flag = True
        chk_list=["0","1","2","3","4","5","6","7","8","9"]
        n = -1
        if len(s) <= 1 :
            if s in chk_list:
                return int(s)
            else :
                return 0
        for val in s:
            if val == " ":
                continue
            else :
                n=s.index(val)
                break
        if n == -1 :
            return 0
        if s[n] == "-":
            flag = False
        if s[n] == "+" or s[n] == "-":
            n += 1
        if s[n] not in chk_list:
            return 0        
        for val in s[n:]:
            if val in chk_list:
                ans_str += val
            else:
                break
        ans = int(ans_str)
        if not flag:
            ans = -1*ans
        if -2**31 <= ans and ans <= 2**31-1:
            return ans
        elif -2**31 > ans:
            return -2**31
        else:
            return 2**31-1

Solution().myAtoi("-99999999999999999999999")
