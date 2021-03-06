# 功能：砝码称重
# 要求：现有一组砝码，重量互不相等，分别为m1,m2,m3…mn；每种砝码对应的数量为x1,x2,x3...xn。
#      现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。称重重量包括0
# 输入格式：输入包含多组测试数据。对于每组测试数据：
#         第一行：n --- 砝码数(范围[1,10])
#         第二行：m1 m2 m3 ... mn --- 每个砝码的重量(范围[1,2000])
#         第三行：x1 x2 x3 .... xn --- 每个砝码的数量(范围[1,6])
# 输出格式：利用给定的砝码可以称出的不同的重量数
# 样例：输入：2
#           1 2
#           2 1
#      输出：5
#      说明：有0,1,2,3,4五种重量。难度较大，稍微理解就好。

def fama(n,weight,nums):
    res = set()
    for i in range(nums[0]+1):
        res.add(i*weight[0])
    for i in range(1, n):
        tmp = list(res)
        for j in range(1, nums[i]+1):
            for wt in tmp:#变成list在这里才能遍历
                res.add(wt+j*weight[i])
    return len(res)


def main():
    while True:
        try:
            n = int(input())
            weight = [int(i) for i in input().split()]
            nums = [int(i) for i in input().split()]
            print(fama(n, weight, nums))
        except:
            break


if __name__ == '__main__':
    main()