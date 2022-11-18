from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        list_calc=[]
        mat_calc=[]
        ans_list=[]
        for val in mat :
            n=0
            for j in val :
                n += j
            list_calc.append(n)
        for i,val in enumerate(list_calc):
            n = [i,val]
            mat_calc.append(n)
        mat_calc.sort(key = lambda x:x[1])
        for val in mat_calc:
            ans_list.append(val[0])
        
        return ans_list[:k]

Solution().kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3)

