# 功能：给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。（思想是动态规划）
# 要求：得到回文字符串。
# 输入格式：输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000。
# 输出格式：最少需要删除的字符个数。
# 样例：输入：abcda
#           google
#      输出：2
#           2
#      说明：第一个字符串删除两个字符，第二个字符串删除两个字符。
import numpy as np
import sys


def palindromic_string(s):
    s_reverse = s[::-1]
    dp = [[0 for i in range(len(s) + 1)] for j in range(len(s) + 1)]   #注意二维数组的赋值方法
    # dp = np.zeros((1001, 1001), dtype=np.int)
    for i in range(1, len(s) + 1, 1):    #动态规划算法
        for j in range(1, len(s) + 1, 1):
            if s[i - 1] == s_reverse[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return len(s) - dp[len(s)][len(s)]


def main():
    while True:
        s = sys.stdin.readline().strip()
        if not s:
            break
        print(palindromic_string(s))


if __name__ == '__main__':
    main()
