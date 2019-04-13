# 功能：分隔字符串
# 要求：字符串按长度为8拆分每个字符串后输出到新的字符串数组；长度不是8整数倍的字符串请在后面补数字0。
# 输入格式：连续输入字符串(输入2次,每个字符串长度小于100)
# 输出格式：输出到长度为8的新字符串数组
# 样例：输入：abc
#           123456789
#      输出：abc00000
#           12345678
#           90000000
#      说明：第一个例子abc需要补0，第二个例子1到8，不需要补0,9需要补0。

import sys


def cut_string(s):
    result = []
    start = 0
    while True:
        if start + 8 < len(s):     #如果不需要补0，直接添加
            s1 = []
            s1.extend(s[start:start + 8])
            start = start + 8
            result.append(s1)
        else:                    #需要补0的情况
            s1 = []
            s1.extend(s[start:len(s)])
            for i in range(len(s1), 8, 1):
                s1.extend('0')
            result.append(s1)
            break
    return result


def main():
    result = []
    n = 2
    while n != 0:
        string = sys.stdin.readline().strip()
        result.append(cut_string(string))
        n = n - 1
    for i in range(len(result)):
        for j in range(len(result[i])):
            print("".join(result[i][j]))


if __name__ == '__main__':
    main()
