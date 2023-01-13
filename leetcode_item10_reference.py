
# 参考サイト　https://redquark.org/leetcode/0010-regular-expression-matching/ から
def isMatch(s: str, p: str) -> bool:
    rows, columns = (len(s), len(p))
    # Base conditions
    if rows == 0 and columns == 0:
        return True
    if columns == 0:
        return False
    # DP array
    dp = [[False for j in range(columns + 1)] for i in range(rows + 1)]
    # Since empty string and empty pattern are a match
    dp[0][0] = True
    # Deals with patterns containing *
    for i in range(2, columns + 1):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 2]
    # For remaining characters
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif j > 1 and p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
    return dp[rows][columns]

isMatch("aaaa","a*a")

dp = [[False for j in range(3)] for i in range(2)]
print(dp)

#上の通りに見ないで自分で書いてみる（動的計画法)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        row = len(s)
        column = len(p)
        dp = [[False for j in range(column+1)] for i in range(row+1)]
        dp[0][0] = True
        # *がある場合のdp[0](=sの先頭の前の空文字列)にpをマッチさせる)
        for j in range(2,column+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        for i in range(1,row+1):
            for j in range(1,column+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif j > 1 and p[j-1] == "*":
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == ".":
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
        return dp[row][column]

Solution().isMatch("aa","a*")



