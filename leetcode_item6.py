class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s 
        mtrx =[]
        for i in range(numRows):
            mtrx.append([]) # mtrx = [[]]*numRowsは入れ子の[]が同じオブジェクトになるのでダメ
        j=0
        for val in s:            
            mtrx[j].append(val)
            if j == 0 :
                flag = 0
            if j < numRows-1 and flag == 0 :
                j += 1
            else:
                j -= 1
                flag = 1
        return mtrx #リストを文字に直す。ロジックはＯＫ

Solution().convert("PAYPALISHIRING",4)





"""
vectorworksで検討する(zigzag_conversion検討.vwx)列方向yのスペースは無視して詰めてＯＫ)
"""

