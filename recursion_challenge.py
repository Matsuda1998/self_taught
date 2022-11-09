#https://leetcode.com/problems/roman-to-integer/
from soupsieve import SoupSieve


class Solution(object):
    def romanToInt(self, s):
        """
        leetcode.comの初めての人用の問題
        :type s: str
        :rtype: int
        """
        roman_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        roman_dict2={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        s_list=[]
        s_pair=[]
        n=0
        for i in range(len(s)):
            s_list.append(s[i])
        for i in range(len(s)-1):
            s_pair.append(s[i]+s[i+1])
        for i in range(len(s_list)-len(s_pair)):
            s_pair.append(None)
        print(s_list)
        print(s_pair)
        while len(s_list) > 0:
            if s_pair[0] in roman_dict2:
                n += roman_dict2[s_pair[0]]
                s_list.pop(0)
                s_pair.pop(0)
            else:
                n += roman_dict[s_list[0]]
            s_list.pop(0)
            s_pair.pop(0)
        return n

s=Solution()
s.romanToInt("MMMCMLXXVI")
#できたので再帰的、オブジェクト指向で作り直す！
class Solution:
    roman_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    roman_dict2={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    def __init__(self,str):
        self.str=str
        self.s_list=[]
        self.s_pair=[]
        self.n=0
        for i in range(len(self.str)):
            self.s_list.append(self.str[i])
        for i in range(len(self.str)-1):
            self.s_pair.append(self.str[i]+self.str[i+1])
        for i in range(len(self.s_list)-len(self.s_pair)):
            self.s_pair.append(None)
    def romanToInt(self,n,sl,sp):
        if len(sl) == 0:
            #print(n)
            return n
        if len(sl) > 0:
            if sp[0] in self.roman_dict2:
                n += self.roman_dict2[sp[0]]
                sl.pop(0)
                sp.pop(0)
            else:
                n += self.roman_dict[sl[0]]
            sl.pop(0)
            sp.pop(0)
            #print(n)
            #print(sl)
            #print(sp)
            return self.romanToInt(n,sl,sp)#再帰的に関数を呼ぶときreturnをつけないと
                                           #関数としての戻り値がNoneになってしまう。
                                           #つけなくても計算そのものはしている(上には戻る)

s=Solution("MMMCMLXXVI")
print(s.romanToInt(s.n,s.s_list,s.s_pair))
type(s.romanToInt(s.n,s.s_list,s.s_pair))

#ループ、オブジェクト指向で作り直す！
class Solution:
    roman_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    roman_dict2={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    def __init__(self,str):
        self.str=str
        self.s_list=[]
        self.s_pair=[]
        self.n=0
        for i in range(len(self.str)):
            self.s_list.append(self.str[i])
        for i in range(len(self.str)-1):
            self.s_pair.append(self.str[i]+self.str[i+1])
        for i in range(len(self.s_list)-len(self.s_pair)):
            self.s_pair.append(None)
    def romanToInt(self):
        while len(self.s_list) > 0:
            if self.s_pair[0] in self.roman_dict2:
                self.n += self.roman_dict2[self.s_pair[0]]
                self.s_list.pop(0)
                self.s_pair.pop(0)
            else:
                self.n += self.roman_dict[self.s_list[0]]
            self.s_list.pop(0)
            self.s_pair.pop(0)
        return self.n

s=Solution("MMMCMLXXVI")
print(s.romanToInt())
