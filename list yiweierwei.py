# list的一维和二维的数组写法

a = [[0 * 10] for i in range(5)]
print(a)

b = [0] * 10
print(b)

a = [[0] * 2]
c = [0] * 2
b = a * 3
d = c * 3
print(b)
print(d)
