# 功能：排队
# 要求：合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，
#      他们的身高分别为T1，T2，…，TK，
#      则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。
#      你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。
# 输入格式：多少个同学，以及每个同学的身高
# 输出格式：输出最少需要请出列的同学个数
# 样例：输入：8
#           186 186 150 200 160 130 197 200
#      输出：4
#      说明：这个题考的是动态规划和最长递增子串

import sys


def di(people):
    result = [0 for i in range(len(people))]
    for i in range(len(people)):
        for j in range(i + 1):
            if people[i] > people[j]:
                if result[i] < result[j] + 1:
                    result[i] = result[j] + 1
        if result[i] == 0:
            result[i] = 1
    return result


def main():
    while True:
        try:
            num = int(sys.stdin.readline().strip())
            people = sys.stdin.readline().strip()
            people = people.split()
            people = [int(people[i]) for i in range(num)]
            left = di(people)
            right = di(people[::-1])
            right = right[::-1]
            number = 0
            for i in range(len(people)):
                if left[i] + right[i] > number:
                    number = left[i] + right[i]
            print(len(people) - number + 1)
        except:
            break


if __name__ == '__main__':
    main()
