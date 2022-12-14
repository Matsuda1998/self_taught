class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s 



"""
s[i]の位置を求める。
s="PAYPALISHIRING"
rows=3
mat_list=[[]]*rows
[0 4 8 2
 1357913
 2 6 0]
raws=2
[0246802
 1357913]
rows=4
[0  6  2
 1 57 13
 24 80
 3  9   ]
rows=5
[0   8   6  
 1  79  57
 2 6 0 4 8
 35  13  9     s[3]=mat_list[3][0],s[5]=mat_list[3][1],s[11]=mat_list[3][3]
 4   2   0]
rows=6
[0    0
 1   91
 2  8 2
 3 7  3
 46   4
 5    5
ros=7
[0     2
 1    1
 2   0
 3  9
 4 8
 57
 6




"""
[[]]*4
