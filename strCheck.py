# 功能：字符串校正
# 要求：1、三个字母连在一起，去掉一个，比如helllo->hello
#      2、两对一样的字母（AABB型）去掉第二对的一个字母，比如helloo->hello
#      3、上面规则优先从左到右匹配，如果是AABBCC，虽然AABB和BBCC都是错误拼写，但是优先考虑修复AABB，结果为AABCC
# 输入格式：第一行是字符串的个数，后面每行为字符串
# 输出格式：每行为校正完的字符串
# 样例：输入：2
#           helllo
#           wooooooow
#      输出：hello
#           woow

import sys


def return_string(string):
    l = len(string)
    n = 0
    i = 0
    while n < l:    #依次进行判断是否符合三个条件中的哪一个
        if i + 2 < len(string) and string[i] == string[i + 1] and string[i] == string[i + 2]:
            del string[i]
            i = i
            n = n + 2
        elif i + 3 < len(string) and string[i] == string[i + 1] and string[i + 2] == string[i + 3]:
            if i + 5 < len(string) and string[i + 4] == string[i + 5]:
                del string[i + 3]
                n = n + 2
                i = i
            else:
                del string[i + 3]
                i = i
                n = n + 2
        else:
            i = i + 1
            n = n + 1
    return string


def main():
    result = []
    number = int(sys.stdin.readline().strip())   #字符串的个数
    while number != 0:
        s = []
        string = sys.stdin.readline().strip()
        for i in range(len(string)):
            s.append(string[i])
        number = number - 1
        result.append("".join(return_string(s)))
    for i in range(len(result)):
        print(result[i])


if __name__ == '__main__':
    main()
