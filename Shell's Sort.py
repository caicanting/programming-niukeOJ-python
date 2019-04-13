# 功能：希尔排序
# 要求：希尔排序
# 输入格式：数字
# 输出格式：数字
# 样例：输入：4,5,1,3
#      输出：1,3,4,5


def main():
    nums = input()
    nums = nums.split(",")
    shell_sort(nums)


def shell_sort(nums):
    n = len(nums)
    gap = n // 2       #对半分
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i - gap) >= 0:
                if nums[i] < nums[i - gap]:  #比较大小，小的放前面，大的放后面
                    nums[i], nums[i - gap] = nums[i - gap], nums[i]
                    i = i - gap
                else:
                    break
        gap = gap // 2
    print(nums)


if __name__ == '__main__':
    main()
