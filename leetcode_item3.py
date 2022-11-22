class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_ans =[]
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            val = s[i]
            j = i
            while j + 1 < len(s):
                if s[j+1] not in val :
                    val += s[j+1]
                    j += 1
                else :
                    break
            list_ans.append(val)
        list_ans.sort(key=len,reverse=1)
        return len(list_ans[0]),list_ans

Solution().lengthOfLongestSubstring("dvdf")
Solution().lengthOfLongestSubstring("abcabcbb")
Solution().lengthOfLongestSubstring("pwwkew")
Solution().lengthOfLongestSubstring("apple_juce")


