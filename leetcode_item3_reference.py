# Sample 46 ms submission
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = -1 #初期値が-1なのはインデックス0の要素が最初に出て来た時ansを"1"にするため
        chars = {}
        ans = 0
        for i,ch in enumerate(s):
            if ch in chars and chars[ch] > j: # and以下は今回の命題だけならいらない。いや、いる！
                                              # jを決めた要素と今回の要素が同じかどうかをチェック
                j = chars[ch] # jをその文字要素が前回出て来たインデックスに合わせる
            else:
                if ans < i-j: #要素と要素の間隔が従来の記録を上回れば
                    ans = i-j # ansを更新
            chars[ch] = i # 文字の要素のインデックスを保存
        return ans

Solution().lengthOfLongestSubstring("dvdf")

# 自分でやってみる
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        j = -1
        ans = 0
        for i , cha in enumerate(s):
            if cha in chars and chars[cha] -j > 0:
                j = chars[cha]
            else :
                if ans < i -j :
                    ans = i -j
            chars[cha] = i
        return ans
Solution().lengthOfLongestSubstring("tmmzuxt")


