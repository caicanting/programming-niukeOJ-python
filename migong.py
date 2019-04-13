# 功能：走迷宫
# 要求：矩阵表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求找出从左上角到右下角的最短路线。入口点为[0,0]。
# 输入格式：输入两个整数，分别表示二位数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。
# 输出格式：左上角到右下角的最短路径。
# 样例：输入：5 5
#           0 1 0 0 0
#           0 1 0 1 0
#           0 0 0 0 0
#           0 1 1 1 0
#           0 0 0 1 0
#      输出：(0,0)
#           (1,0)
#           (2,0)
#           (2,1)
#           (2,2)
#           (2,3)
#           (2,4)
#           (3,4)
#           (4,4)

import sys


def zou_mi_gong(s):
    result = []
    result.append([0, 0])
    i = 0
    j = 0
    while [len(s) - 1, len(s[0]) - 1] not in result:
        if i + 1 < len(s) and s[i + 1][j] == '0':
            result.append([i + 1, j])
            i = i + 1
        elif j + 1 < len(s[0]) and s[i][j + 1] == '0':
            result.append([i, j + 1])
            j = j + 1
        else:      #一直回溯，直到条件满足，继续往下执行
            hang = result[-1][0]
            while True:
                while result[-1][0] == hang:
                    del result[-1]
                i = result[-1][0]
                j = result[-1][1]
                if j + 1 < len(s[0]) and s[i][j + 1] == '0':
                    result.append([i, j + 1])
                    j = j + 1
                    break
                else:
                    hang = result[-1][0]
    for i in range(len(result)):
        print('(' + str(result[i][0]) + ',' + str(result[i][1]) + ')')


def main():
    while True:
        try:
            row_col = sys.stdin.readline().strip().split()
            if row_col == '':
                break
            mi_gong = []
            for i in range(int(row_col[0])):
                s = sys.stdin.readline().strip().split()
                s = [s[i] for i in range(len(s))]
                mi_gong.append(s)
            zou_mi_gong(mi_gong)
        except:
            break


if __name__ == '__main__':
    main()
