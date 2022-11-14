from typing import List  #これをインポートしないとlistの要素を型アノテーションできない
                         #nums:list はなくてもよいがnums:List[int]は上式が必要
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_list=[]
        for j,val in enumerate(nums) :
            #if j == len(nums)-1:  この式はいらない。下のfor文でrange(a,b)a=b
            #    break　　　　　　　 はエラーにならす空のrangeオブジェクトを返す
            for i in range(j+1,len(nums)):
                if val+nums[i] == target:
                    ans_list.append(j)
                    ans_list.append(i)
                    return ans_list
        print("nums is invalid list!")


Solution().twoSum([1,2,7,11],9)



