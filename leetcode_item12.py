class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dic=[{"1":"I","2":"II","3":"III","4":"IV","5":"V","6":"VI","7":"VII","8":"VIII","9":"IX"},
                   {"1":"X","2":"XX","3":"XXX","4":"XL","5":"L","6":"LX","7":"LXX","8":"LXXX","9":"XC"},
                   {"1":"C","2":"CC","3":"CCC","4":"CD","5":"D","6":"DC","7":"DCC","8":"DCCC","9":"CM"},
                   {"1":"M","2":"MM","3":"MMM"}]
        new_num = num
        roman_str = ""
        for i in reversed(range(4)):
            temp=new_num // 10**i
            if temp != 0 :
                temp = str(temp)
                roman_str += roman_dic[i][temp]
            new_num = new_num % 10**i
        return roman_str

Solution().intToRoman(1)
print(list(reversed(range(4))))      