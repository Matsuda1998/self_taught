# Sample 46 ms submission
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = -1 #初期値が-1なのはインデックス0の要素が最初に出て来た時ansを"1"にするため
        chars = {}
        ans = 0
        for i,ch in enumerate(s):
            if ch in chars and chars[ch] > j: # and以下は今回の命題だけならいらない。一般化すれば必要
                j = chars[ch] # jをその文字要素が前回出て来たインデックスに合わせる
            else:
                if ans < i-j: #要素と要素の間隔が従来の記録を上回れば
                    ans = i-j # ansを更新
            chars[ch] = i # 文字の要素のインデックスを保存
        return ans

Solution().lengthOfLongestSubstring("dvdf")