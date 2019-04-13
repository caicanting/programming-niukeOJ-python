# 功能：高精度加法
# 要求：高精度加法
# 输入格式：输入两个字符串，第一行输入一个字符串和一个空格，第二行输入一个字符串
# 输出格式：输出结果
# 样例：输入：9876543210加个空格
#           1234567890
#      输出：11111111100


def gaojingdu_add(num1, num2):
    result = []
    count = 0
    for i in range(len(num1) - 1, 0, -1):
        if int(num1[i]) + int(num2[i]) + count >= 10:
            result.append(str(int(num1[i]) + int(num2[i]) + count - 10))
            count = 1
        else:
            result.append(str(int(num1[i]) + int(num2[i]) + count))
            count = 0
        if i == 1 and count == 1:
            result.append('1')
    result.reverse()
    if num1[0] == '-':
        result.insert(0, '-')
    return ''.join(result)


def main():
    while True:
        try:
            num1 = input()
            if num1 == '':
                break
            num2 = input()
            num1 = [num1[i] for i in range(len(num1))]
            num1.remove(' ')
            num2 = [num2[i] for i in range(len(num2))]
            if num1[0].isdigit():
                num1.insert(0, '+')
            if num2[0].isdigit():
                num2.insert(0, '+')
            if len(num1) < len(num2):
                while len(num1) < len(num2):
                    num1.insert(1, '0')
            else:
                while len(num1) > len(num2):
                    num2.insert(1, '0')
            print(gaojingdu_add(num1, num2))
        except:
            break


if __name__ == '__main__':
    main()