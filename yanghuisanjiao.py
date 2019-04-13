# 功能：杨辉三角的变形，计算偶数出现的位置
# 要求：第一行只有一个数1，以下每行的每个数，是恰好是它上面的数，左上角数到右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。
#      求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。
# 输入格式：输入一个整数表示第几行
# 输出格式：输出一个整数，表示该行的第几个
# 样例：输入：4
#      输出：3
#      说明：见如下图。
#             1
#
#          1  1  1
#
#       1  2  3  2  1
#
#    1  3  6  7  6  3  1
#
# 1  4  10 16 19  16 10  4  1


def compute_index(n):
    d = [[0 for i in range(1)] for j in range(n + 1)]
    d[1].append(1)
    for i in range(2, n + 1):
        for j in range(2 * i - 1):
            if j - 2 <= 0:
                d[i].append(sum(d[i - 1][1: j + 2]))
            elif j + 2 > len(d[i - 1]):
                d[i].append(sum(d[i - 1][j - 1:]))
            else:
                d[i].append(sum(d[i - 1][j - 1:j + 2]))
    for i in range(1, len(d[n])):
        if d[n][i] % 2 == 0:
            return i
    return -1

def main():
    while True:
        try:
            n = int(input())
            if n == '':
                break
            print(compute_index(n))
        except:
            break


if __name__ == '__main__':
    main()
