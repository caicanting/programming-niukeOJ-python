# 功能：给字符串排序
# 要求：把字符串按ASCII码从小到大排列，不能两个一样的字母排在一起
# 输入格式：字符串
# 输出格式：字符串
# 样例：输入：e,e,e,f,f,g,h,h,h
#      输出：efghefheh


def str_sort(str_list):
    str_list.sort()
    i = 0
    while i != len(str_list):
        if str_list[i] == str_list[i - 1]:     #如果两个字符一样，则把其中一个字符放到列表后面，然后删除这个字符
            str_list.append(str_list[i])
            del(str_list[i])
        else:
            i = i + 1
    print("输出排序后的字符串")
    print("".join(str_list))


def main():
    print("请输入字符串，用','隔开,如(e,e,f)")
    str_list = input()
    str_list = str_list.split(",")
    str_sort(str_list)


if __name__ == '__main__':
    main()
