# 功能：输出字典的键和值
# 要求：将相同索引的数值进行求和运算，输出按照key值升序进行输出。
# 输入格式：先输入键值对的个数，然后输入成对的index和value值，以空格隔开
# 输出格式：输出合并后的键值对（多行）
# 样例：输入：4
#           0 1
#           0 2
#           1 2
#           3 4
#      输出：0 3
#           1 2
#           3 4
#      说明：两个键为0的值合并，再按键的升序排列。
import sys


def main():
    d = {}
    n = int(sys.stdin.readline().strip())
    while n != 0:
        s = sys.stdin.readline().strip().split()
        s = [int(s[i]) for i in range(len(s))]
        if s[0] in d:
            d[s[0]] = int(s[1]) + d[s[0]]
        else:
            d[s[0]] = int(s[1])
        n = n - 1
    d2 = sorted(d.items(), key=lambda x: x[0])
    d2 = list(d2)
    for i in range(len(d2)):
        print(d2[i][0], d2[i][1])


if __name__ == '__main__':
    main()
