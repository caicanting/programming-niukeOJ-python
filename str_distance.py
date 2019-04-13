# 功能：计算字符串距离
# 要求：一个转换成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。
# 输入格式：输入两个字符串
# 输出格式：输出最少的操作数
# 样例：输入：abcdefg
#           abcdef
#      输出：1
#      说明：只需要把最后一个字符操作。


def editDistance(str1, str2):
    m, n = len(str1) + 1, len(str2) + 1
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        dp[i][0] = i
    for j in range(n):
        dp[0][j] = j
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]))
    return dp[-1][-1]

def main():
    while True:
        try:
            str1 = input()
            if str1 == '':
                break
            str2 = input()
            print(editDistance(str1, str2))
        except:
            break

if __name__ == '__main__':
    main()