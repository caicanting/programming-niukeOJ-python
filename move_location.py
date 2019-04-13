# 功能：移动坐标。
# 要求：A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动。
# 输入格式：输入一个字符串，合法坐标为A(或者D或者W或者S)+数字（两位以内）坐标之间以;分隔。非法坐标点需要进行丢弃。
# 输出格式：最终坐标，以,分隔
# 样例：输入：A10;S20;W10;D30;X;A1A;B10A11;;A10;
#      输出：10,-10

import sys


def move(s):
    result = [0, 0]
    string = ['A', 'D', 'W', 'S']
    i = 0
    while i != len(s):
        if (len(s[i]) > 3) or (len(s[i]) < 2) or s[i][0] not in string:
            del s[i]
        elif len(s[i]) == 2 and s[i][1].isdigit():
            i = i + 1
        elif len(s[i]) == 3 and s[i][1].isdigit() and s[i][2].isdigit():
            i = i + 1
        else:
            del s[i]
    for i in range(len(s)):
        if s[i][0] == 'A':
            result[0] = result[0] - int(s[i][1:])
        elif s[i][0] == 'D':
            result[0] = result[0] + int(s[i][1:])
        elif s[i][0] == 'S':
            result[1] = result[1] - int(s[i][1:])
        elif s[i][0] == 'W':
            result[1] = result[1] + int(s[i][1:])
    result = [str(result[i]) for i in range(len(result))]
    return ','.join(result)


def main():
    while True:
        s = sys.stdin.readline().strip()
        if s == "":
            break
        s = s.split(";")
        print(move(s))


if __name__ == '__main__':
    main()
