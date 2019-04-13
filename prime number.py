# 功能：质数因子
# 要求：按照从小到大的顺序输出它的所有质数的因子。
# 输入格式：输入一个long型整数
# 输出格式：按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
# 样例：输入：180
#      输出：2 2 3 3 5
import sys
import math


def is_prime(number):
    if number == 2:
        return True
    else:
        for j in range(2, int(math.ceil(number ** 0.5)), 1):
            if number % j == 0:
                return False
        return True


def prime_element(number):
    if is_prime(number):
        print(number, end=' ')
    else:
        result = []
        prime_number = [2]
        for i in range(3, number // 2 + 1, 1):
            if is_prime(i):
                prime_number.append(i)
        i = 0
        while number != 1:
            if number % prime_number[i] == 0:
                result.append(prime_number[i])
                number = number // prime_number[i]
            else:
                i = i + 1
        for k in range(len(result)):
            print(result[k], end=' ')


def main():
    number = int(sys.stdin.readline().strip())
    prime_element(number)


if __name__ == '__main__':
    main()

