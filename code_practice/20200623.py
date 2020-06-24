#6.22 Python代码练习


# 英制单位英寸和公制单位厘米互换
# print('英制单位英寸和公制单位厘米互换:')
# value = float(input('请输入长度：'))
# unit = input('请输入单位：')
# if unit == 'in' or unit =='英寸':
#     print('%f英寸 = %f厘米' %(value, value*2.54))
# elif unit =='cm' or unit =='厘米':
#     print('%f厘米 = %f英寸' %(value, value/2.54))
# else:
#     print('请输入有效单位：')

# 输入三条边长，如果能构成三角形就计算其周长和面积
# print('输入三条边长，如果能构成三角形就计算其周长和面积:')
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c > a:
#     p = (a + b + c)/2
#     area = (p*(p-a)*(p-b)*(p-c))**0.5
#     print('circumfence = ', a + b + c)
#     print('area = ',area)
#     print('circumfence = %f,area = %f' %(a+b+c,area))
# else:
#     print('Error')

# 水仙花数
# print('水仙花数')
# for num in  range(100,1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid **3 + high**3:
#         print(num)
# print('')

#while循环：猜数
# import random
# answer = random.randint(1,100)
# count = 0
# while True:
#     count += 1
#     num = int(input('please input:'))
#     if num > answer:
#         print('too bigger')
#     elif num < answer:
#         print('too smaller')
#     else:
#         print('it`s right!，the answer is:',answer)
#         break
# print('total:%d' %count)
# if count > 5:
#     print('stupid!')

#while:九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d' %(i, j, i*j),end='\t')
#     print()

#输入一个正整数判断它是不是素数
# from math import sqrt
# num = int(input('please input a number:'))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d is prime' % num)
# else:
#     print('%d is not prime' % num)

#输入0-100内的素数
# from math import sqrt
# for i in range(0,101):
#     is_prime = True
#     for j in range(2, int(sqrt(i))+1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime and i != 1:
#         print('%d' % i)

#打印三角形图案
# row = int(input('please input the counts of line: '))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')
#     print()

# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()

#生成斐波那契数列的前20个数
# a = 0
# b = 1
# for _ in range(20):
#     a, b = b, a + b
#     print(a, end=' ')

#找出10000以内的完美数
#完美数是除自身外其他所有因子的和正好等于这个数本身的数
import math
for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)
