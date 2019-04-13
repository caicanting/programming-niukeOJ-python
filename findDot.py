# 功能：找点的个数
# 要求：二维平面整数点集。定义某点x，如果x满足任意点都不在x的右上方区域内，求出所有点的集合。
# 输入格式：多少个点，依次输入每个点的横坐标和纵坐标
# 输出格式：找到的点的横坐标和纵坐标
# 样例：输入：5
#           1 2
#           5 3
#           4 6
#           7 5
#           9 0
#      输出：4 6
#           7 5
#           9 0
#      说明：有5个点，(1, 2)...(9, 0)，最后符合条件的点只有(4, 6),(7, 5),(9, 0)。


def find_dot(dots):
    dots.sort(reverse=True)   #从大到小排序
    m = dots[0][1]
    j = 1
    while j < len(dots):
        if dots[j][1] > m:    #比较每个点的纵坐标大小
            m = dots[j][1]
            j = j + 1
        else:
            del dots[j]     #不符合条件的点删除
    print("输出所有符合要求的点的坐标")
    for k in range(len(dots) - 1, -1, -1):
        print(dots[k][0], dots[k][1])


def main():
    xy_nums = []     #所有点的坐标
    print("请输入点的个数")
    dot_number = int(input())   #点的个数
    while dot_number != 0:
        print("请输入该点的坐标，如1 2(表示x轴是1，y轴是2，空格隔开)")
        dot = input()
        dot = dot.split(" ")
        dot = [int(dot[i]) for i in range(len(dot))]
        xy_nums.append(dot)
        dot_number = dot_number - 1
    find_dot(xy_nums)


if __name__ == '__main__':
    main()
