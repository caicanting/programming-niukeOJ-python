# 功能：裁剪绳子，让绳子长度相等
# 要求：有n根绳子，第i根绳子长度为li，现在需要m根等长的绳子，你可以对n根绳子进行任意裁剪,不能拼接
# 输入格式：第一行输入两个数，n和m，第二行输入n个数表示绳子的长度
# 输出格式：输出裁剪后的最长长度，保留两位小数
# 样例：输入：3 4
#           3 5 4
#      输出：2.5
#      说明：切割的绳子最大长度为2.5。
import sys


def cut_rope(end_number, l):
    number_rope = []
    max_length = "%.2f" % (sum(l) / end_number)
    number_rope.append([(l[i] // float(max_length)) for i in range(len(l))])
    if sum(number_rope[0]) == end_number:
        print("输出绳子的最大长度")
        print(max_length)
    else:
        max_length = 0
        for i in range(len(l)):
            length = l[i] / (number_rope[0][i] + 1)
            if max_length <= length:
                max_length = length
        print("输出绳子的最大长度")
        print("%.2f" % max_length)


def main():
    print("请输入原始的绳子根数和最终需要的绳子根数，用空格隔开（如，3 4）")
    number = sys.stdin.readline().strip()
    ori_number = int(number[0])
    end_number = int(number[2])
    print("输入原始绳子的长度")
    l = sys.stdin.readline().strip()
    l = l.split(' ')
    l = [int(l[i]) for i in range(ori_number)]
    cut_rope(end_number, l)


if __name__ == '__main__':
    main()
