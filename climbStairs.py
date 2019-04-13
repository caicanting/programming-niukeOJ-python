# 功能：计算爬台阶最少需要的步数
# 要求：每次最少走一步，最多的步数是该台阶上对应输入的步数
# 输入格式：多少个台阶，依次输入在每个台阶上能走的最大步数
# 输出格式：输出最少的步数
# 样例：输入：2
#           2
#           1
#      输出：1
#      说明：有两个台阶，第一个最多可以走两步，第二个最多可以走一步，只需要走一次（两步），就爬完台阶。


#爬台阶的子函数
def climb_stairs(number_stairs, stairs):     #n表示台阶数，nums表示每个台阶上能走的最大步数的列表（数组）
    end = number_stairs
    result = 0     #result是走的步数
    while end != 1:
        for i in range(end):    #从第一个台阶开始找，找到能一步到end台阶，即将找到的台阶设置为end台阶，依次类推遍历
            if stairs[i] + i + 1 >= end:
                end = i + 1
                result = result + 1
                break
    print("需要的最少步数是")
    print(result)


def main():
    stairs = []     #存放台阶步数的列表
    print("请输入台阶数")
    n_stairs = int(input())   #表示台阶数
    total = 0
    while total != n_stairs:    #依次循环输入所有台阶数
        print("请输入第" + str(total) + "个台阶的最大步数")
        stair = input()
        stairs.append(int(stair))
        total = total + 1
    climb_stairs(n_stairs, stairs)


if __name__ == '__main__':
    main()
