# 功能：计算最少需要多少个硬币
# 要求：有钱数m，和n种面额的硬币，计算m，最少需要多少个硬币，如果不行，则输出-1
# 输入格式：第一行输入m和n，接下来n行输入n种硬币的面额
# 输出格式：输出最少需要多少个硬币
# 样例：输入：20 4
#           1
#           2
#           5
#           10
#      输出：2
#      说明：(10, 10)这两个硬币就可以得到m的总钱数。
import sys


def coin(m, all_money):
    total = m
    flag = 0
    add_coin = [0 for i in range(m)]
    if m in all_money:
        add_coin.clear()
        add_coin.append(m)
        return len(add_coin)
    else:
        for j in range(len(all_money) - 1, -1, -1):    #计算每种方案的硬币个数
            every_time = []
            if all_money[j] <= m:
                j_n = m // all_money[j]
                every_time.extend([all_money[j]] * j_n)
                m = m - j_n * all_money[j]
                if m == 0:
                    flag = 1
                    if len(every_time) < len(add_coin):
                        add_coin.clear()
                        add_coin.extend(every_time)
                    break
            for i in range(j - 1, -1, -1):
                if all_money[i] <= m:
                    i_n = m // all_money[i]
                    every_time.extend([all_money[i]] * i_n)
                    m = m - i_n * all_money[i]
                    if m == 0:
                        if len(every_time) < len(add_coin):
                            add_coin.clear()
                            add_coin.extend(every_time)
                    flag = 1
                    break
            m = total
    if flag == 0:
        return -1
    return len(add_coin)


def main():
    while True:
        try:
            m_n = sys.stdin.readline().strip().split()
            m = int(m_n[0])
            n = int(m_n[1])
            all_money = []
            for i in range(n):
                money = int(sys.stdin.readline().strip())
                all_money.append(money)
            all_money.sort()
            print(coin(m, all_money))
        except:
            break


if __name__ == '__main__':
    main()

