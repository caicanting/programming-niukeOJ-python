# 功能：一个由字母和数字组成的字符串，和一个字符，然后输出输入的字符串中含有该字符的个数。不区分大小写。
# 要求：得到个数。
# 输入格式：输入一个有字母和数字以及空格组成的字符串，和一个字符。
# 输出格式：输出输入字符串中含有该字符的个数。
# 样例：输入：aASDFS
#           A
#      输出：2
#      说明：A的大小写有两个。

import sys


def main():
    s = sys.stdin.readline().strip()
    char = sys.stdin.readline().strip()
    if char.isalpha():
        print(s.count(char.upper()) + s.count(char.lower()))
    else:
        print(s.count(char))


if __name__ == '__main__':
    main()
