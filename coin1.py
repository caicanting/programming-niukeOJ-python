# 功能：计算最少需要多少个硬币
# 要求：有m总钱数，和n种面额的硬币，计算从1到m，最少需要多少个硬币，如果不行，则输出-1
# 输入格式：第一行输入m和n，接下来n行输入n种硬币的面额
# 输出格式：输出最少需要多少个硬币
# 样例：输入：20 4
#           1
#           2
#           5
#           10
#      输出：5
#      说明：(1, 2, 2, 5, 10)这五个硬币就可以包含1到m的总钱数。
import sys


def coin(m, all_money):
    flag = 0
    add_coin = []
    for i in range(1, m + 1):
        if sum(add_coin) >= i:
            flag = i
            continue
        elif i in all_money:
            flag = i
            add_coin.append(i)
        else:
            sheng = sum(add_coin)
            sheng_coin = []
            for j in range(len(all_money)):    #一个个计算，直到找到所需个数最少的方法
                if all_money[j] < i:
                    coin_n = 1
                    while coin_n != 0:
                        if coin_n * all_money[j] + sheng >= i:
                            flag = i
                            if len(sheng_coin) == 0:
                                sheng_coin.append(all_money[j] * coin_n)
                                coin_n = 0
                            else:
                                sheng_coin.clear()
                                sheng_coin.append(all_money[j] * coin_n)
                                coin_n = 0
                        else:
                            coin_n = coin_n + 1
                else:
                    break
            add_coin.extend(sheng_coin)
        if flag != i:
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

