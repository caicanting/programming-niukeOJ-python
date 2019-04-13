# 功能：字符串的最后一个单词的长度。
# 要求：得到最后一个单词的长度，字符串的单词以空格隔开。
# 输入格式：一行字符串，非空，长度小于5000。
# 输出格式：整数N，最后一个单词的长度。
# 样例：输入：hello world
#      输出：5
#      说明：最后一个单词是world，所以长度是5。

import sys


def main():
    length = 0
    s = sys.stdin.readline().strip()
    # s = s.split()      #解法二，直接把单词分隔
    # print(len(s[-1]))
    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            length = length + 1
        else:
            break
    print(length)


if __name__ == '__main__':
    main()
