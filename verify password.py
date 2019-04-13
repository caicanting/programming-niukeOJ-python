# 功能：验证密码是否合格
# 要求：1.长度超过8位，2.包括大小写字母.数字.其它符号,以上四种至少三种，3.不能有相同长度超2的子串重复
# 输入格式：一组或多组长度超过2的子符串。每组占一行。
# 输出格式：如果符合要求输出：OK，否则输出NG
# 样例：输入：021Abc9000
#           021Abc9Abc1
#           021ABC9000
#           021$bc9000
#      输出：OK
#           NG
#           NG
#           OK


import sys


def find_repeat(s):   #判断字符串是否有重复子串
    for i in range(len(s) - 5):
        for j in range(i + 1, len(s) - 2):
            if s[i] == s[j]:
                if s[i + 1] == s[j + 1]:
                    if s[i + 2] == s[j + 2]:
                        return True
    return False


def yan_zheng(s):
    if len(s) < 9:
        return 'NG'
    code = []
    for i in range(len(s)):
        if s[i].isdigit():
            if 'digit' not in code:
                code.append('digit')
        elif s[i].islower():
            if 'lower' not in code:
                code.append('lower')
        elif s[i].isupper():
            if 'upper' not in code:
                code.append('upper')
        elif 'other' not in code:
            code.append('other')
    if len(code) < 3:
        return 'NG'
    if find_repeat(s):
        return 'NG'
    else:
        return 'OK'


def main():
    while True:
        s = sys.stdin.readline().strip()
        if s == "":
            break
        print(yan_zheng(s))


if __name__ == '__main__':
    main()
