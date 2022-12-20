class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s[0] != p[0] and p[0] != ".":
            return False
        elif len(s) == 1 and len(p) == 1 : # pの長さ2以上でも大丈夫？完全に一致するものだけｏｋと仮定
            return True
        elif len(s) > 1 and len(p) == 1 :
            return False
        j = 1
        for i in range(1,len(s)): #ここから先全面見直し
            if s[i] == p[j] or p[j] == ".":
                j += 1
                #if j >= len(p):
                    #return False
                continue
            elif p[j] == "*":
                if p[j-1] == ".":
                    return True
                if s[i] == p[j-1]:
                    continue
                elif s[i] == p[j+1]:
                    j += 1
                    if j >= len(p):
                        return False
                    continue
                else:
                    return False
            else:
                return False
        return True


Solution().isMatch("aabcd","aabcd")
"""マッチするパターンを考える(sとpが完全に一致するものだけＯＫと仮定)
s| aabcd p| aabcd .*bcd ..bcd a*..d
"""