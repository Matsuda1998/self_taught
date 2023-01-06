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
            if (s[i] == p[j] or p[j] == ".") and j < len(p) :
                if j < len(p)-1:
                    j += 1
                continue
            elif p[j] == "*":
               if s[i] == p[j-1] or p[j-1] == ".":
                continue
            else:
                return False
        return True

"""違う発想で書いてみる。→pを文字列化(アルファベットのみ)にしsと==だったらTrueを返すというコード
やっぱダメ。sと比べながらでないと･･･
s "a a a" " a a" "a a" "a b" "a b c d"   "a b c d"   "a a b"
p "a * a" " a "  "a *" ". *" "a b c d e" "c . b c d" "c * a * b"
  true    false  true  true  false       false       true
アスタリスクの前は無くてもよい(上の一番右)。これで考える
"""


Solution().isMatch("aabcc","aabc")

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        new_s = ""
        j = 0
        for i in range(len(p)):
            if j == len(s):
                new_s += p[i]
            elif p[i] == s[j] or p[i] == ".":
                new_s += s[j]
                j += 1
            elif p[i] == "*" and p[i-1] != ".":
                t = p[i-1]
                while t == s[j] and j < len(s):
                    new_s += s[j]
                    j += 1
                    if j == len(s):
                        break
            elif p[i] == "*" and p[i-1] == ".":
                if i == len(p)-1:
                    return True
                u = p[i+1]
                while u != s[j] and j < len(s):
                    new_s += s[j]
                    j += 1
                    if j == len(s):
                        break                
        return new_s == s
Solution().isMatch("abcd","c.bcd") # Falseになるようにする

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        new_s = ""
        j = 0
        for i in range(len(p)):
            if j == len(s):
                new_s += p[i]
            elif p[i] == s[j] or p[i] == ".":
                new_s += s[j]
                j += 1
            elif p[i] == "*" and p[i-1] != ".":
                t = p[i-1]
                while t == s[j] and j < len(s):
                    new_s += s[j]
                    j += 1
                    if j == len(s):
                        break
            elif p[i] == "*" and p[i-1] == ".":
                if i == len(p)-1:
                    return True
                u = p[i+1]
                while u != s[j] and j < len(s):
                    new_s += s[j]
                    j += 1
                    if j == len(s):
                        break           
            else :
                new_s += p[i]
                j += 1     
        return new_s == s
Solution().isMatch("abcd","c.bcd") # Falseになる=正解

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        new_s = ""
        j = 0
        for i in range(len(p)):
            if j == len(s):
                new_s += p[i]
            elif p[i] == s[j] or p[i] == ".":
                new_s += s[j]
                j += 1
            elif p[i] == "*" and p[i-1] != ".":
                t = p[i-1]
                while t == s[j] and j < len(s):
                    new_s += s[j]
                    j += 1
                    if j == len(s):
                        break
            elif p[i] == "*" and p[i-1] == ".":
                if i == len(p)-1:
                    return True
                u = p[i+1]
                while u != s[j] and j < len(s):
                    new_s += s[j]
                    j += 1
                    if j == len(s):
                        break
            elif p[i+1] == "*" and i < len(p)-1: # i<len(p)-1をandの左側へ持って行くべき
                continue           
            else :
                new_s += p[i]
                j += 1     
        return new_s == s
Solution().isMatch("aab","c*a*b") # Trueになるように→Ok

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        new_s = ""
        j = 0
        for i in range(len(p)):
            if p[i] == s[j] or p[i] == ".":
                new_s += s[j]
                j += 1
            elif p[i] == "*" and p[i-1] != ".": # i=0のときは無し *の前後同じ文字の時は.*と同じ処理が必要
                t = p[i-1]
                if t == s[j]: # jの位置常に大丈夫か？
                    while j < len(s) and t == s[j]: # j < len(s)を先に(string out of rangeを避ける)
                        new_s += s[j]
                        j += 1
                else:
                    continue # *の0回繰り返しを表現
            elif p[i] == "*" and p[i-1] == ".": # i=0のときは無し この処理あってる？
                if i == len(p)-1:
                    return True
                u = p[i+1]
                while j < len(s) and u != s[j]:
                    new_s += s[j]
                    j += 1
            elif i < len(p)-1 and p[i] != s[j] and p[i] != "." and p[i+1] == "*": # i=0のとき次に*が来ないと成立しない、0<iのときは？
                continue
            else:
                return False
            if j == len(s): # jはlen(s)まで進む ここ考える s < pのとき正しくない
                break
        if i < len(p)-1 : #この式を入れると"aaa","a*a"がおかしくなる。＊のときのパターンをもっと考える
            return False
        else:
            return new_s == s
Solution().isMatch("aaa",".*a")

#アスタリスクのパターンを考え書き直してみる
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = p.count("*")
        index_list = []
        new_s_list = []
        n = m -1
        for i in range(m):
            index_list.append(([0]*3**n+[1]*3**n+[2]*3**n)*3**i)
            n -= 1
        lp = len(p)
        i  = 0
        ls = len(s)
        j  = 0
        if m == 0 and lp != ls: # m==0のときのループもいる？いる。179行がエラーになる
            return False
        if m == 0 :
            index_list =[[1]]
        for x in range(len(index_list[0])): # この位置じゃない？ここだと無限ループ？
            new_s = ""
            y = 0
            while i+1 < lp and j+1 < ls:
                if p[i] != s[j] and p[i] != "." and p[i+1] != "*":
                    return False
                if (p[i] == s[j] or p[i] == ".") and p[i+1] != "*":
                    new_s += s[j]
                    i += 1
                    j += 1
                    continue
                if p[i+1] == "*":
                    if index_list[y][x] == 0:
                        if i+2 < lp and p[i+2] == s[j]:
                            new_s += s[j]
                            i += 3
                            j += 1
                            y += 1
                        else:
                            new_s += "$"
                            break
                    if index_list[y][x] == 1:
                        if p[i] == s[j] or p[i] == ".":
                            new_s += s[j]
                            i += 2
                            j += 1
                            y += 1
                        else:
                            new_s += "$"
                            break
                    if index_list[y][x] == 2:
                        if i+2 < lp and p[i] == s[j]:
                            while p[i] == s[j]:
                                new_s += s[j]
                                j += 1
                            i += 2
                            y += 1
                        elif i+1 == lp and p[i] == s[j]:
                            while p[i] == s[j]:
                                new_s += s[j]
                                j += 1
                            if j == j-1 :
                                new_s += s[j]
                        elif i+1 == lp and p[i] == ".":
                            return True
                        elif i+2 < lp and p[i] == ".": #ここがわからん
                            """ s:abab 
                                p:.*b最初のbを避ける方法"""



                        pass
            if i+1 == lp and j+1 == ls and (p[i] == s[j] or p[i] == "."):
                new_s += s[j]
            if "$" not in new_s :
                new_s_list.append(new_s)
        for ans in new_s_list :
            if ans == s :
                return True
            else:
                continue
        else :
            return False

Solution().isMatch("ababa","ab.bb")
        

            

                    
                        




l=[0]*3**2+[1]*3**2+[2]*3**2
l=[0]*3**2+[1]*3**2+[2]*3**2
l=[0,1,2]*3**0
l=[0,1,2]*3**1
m = 2
l=[[]]*m
print(l)
l[0]=([0]*3**1+[1]*3**1+[2]*3**1)*3**0
l[1]=([0]*3**0+[1]*3**0+[2]*3**0)*3**1
print(l)
m = 3
l=[[]]*m
l[0]=([0]*3**2+[1]*3**2+[2]*3**2)*3**0
l[1]=([0]*3**1+[1]*3**1+[2]*3**1)*3**1
l[2]=([0]*3**0+[1]*3**0+[2]*3**0)*3**2
print(l)
m = 2
index_list = []
n = m -1
for i in range(m):
    index_list.append(([0]*3**n+[1]*3**n+[2]*3**n)*3**i)
    n -= 1
print(index_list)
len(index_list[0])

for i in range(1):
    print(i)







