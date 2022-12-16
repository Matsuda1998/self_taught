class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            flag = True
        else:
            flag = False
        x =abs(x)
        x_str=str(x)
        reverse_str =x_str[::-1]
        x_reverse = int(reverse_str)
        if not flag :
            x_reverse = -1 * x_reverse
        if -2**31 <= x_reverse and  x_reverse <= 2**31 - 1:
            return x_reverse
        else:
            return 0
Solution().reverse(-123)