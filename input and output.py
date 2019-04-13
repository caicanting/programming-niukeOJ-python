# 第一种
# n = input()
# a = input()
# a = [a for a in a]
# print(a)
#
# 10
# 458756
# ['4', '5', '8', '7', '5', '6']



# 第二种
# n = input()
# a = input()
# a = a.split(",")
# a = [int(a[i]) for i in range(int(n))]
# print(a)
#
# 5
# 1,2,3,4,5,6,7,8
# [1, 2, 3, 4, 5]



# 第三种
# a = input()
# a = [a for a in a]
# print(a)
#
# 123456
# ['1', '2', '3', '4', '5', '6']



# 第四种
# flag = True
# n = int(input())
# nums = []
# while flag:
#     a = input()
#     nums.append(a)
#     n = n - 1
#     if n == 0:
#         flag = False
# print(nums)
#
# 5
# 1
# 2
# 3
# 4
# 5
# ['1', '2', '3', '4', '5']

import sys
n = int(sys.stdin.readline().strip())

list = ['1', '2', '3', '4']
list = [int(list[i]) for i in range(len(list))]
print(list)
print("".join(list))


if __name__ == '__main__':
    main()

# 有多组测试样例的，考虑需要加异常判断，try   except
