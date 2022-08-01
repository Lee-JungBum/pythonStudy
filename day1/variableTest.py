# iNum = 10000000000000000000000000000000000000000000000000000000000
# print(type(iNum))
# fNum = 0.123#8Byte
# print(type(fNum))
#
# print(type(1<-2))
#
# _str = 'abc'
#
# print(type(_str))
#
# a=100+30j # 복소수표현법
# print(type(a))

#
# import math
# a = 100
# b = 3
#
# print(math.pow(a,b))    #무조건 소수
# print(a**b) #타입알아서
# print(math.sqrt(2))
# print(2**0.5) #이것도 루트
#
# ans = a/b
# print(ans)
# ans = a%b
# print(ans)
# ans = a//b
# print(ans)
#
# print(int(a/b)) #이게제일빠름
# print(divmod(a,b))
#
# x02 = 0b100000
# x08 = 0o40
# x10=32
# x16 = 0x20
# print(x02,x08,x10,x16)
# print(bin(x10))
# print(oct(x10))
# print(hex(x10))

# a = 5
# b = 3
# print(a&b)
# print(a|b)
# print(a^b)
# print(~b)
#
# a = ['a','b','c']
# n= 3
# for i in range(1<<n):
#     print('{', end=' ')
#     for j in range(n):
#         if i & (1<<j):
#             print(a[j], end = " ")
#     print('}')
#
# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range(2,n):
#         if n%i ==0:
#             return False
#     return True
#
# # a= 3
# # if isPrime(a):
# #     print('소수')
# # else:
# #     print('비소수')
# def isPrime2(n): #확인
#     if n == 1:
#         return False
#     _len = int(n**0.5) #루트를 치하고 정수부분까지만 곱하면된다.
#     for i in range(2,_len+1):
#         if n%i ==0:
#             return False
#     return True
# #
# # a= 3
# # if isPrime2(a):
# #     print('소수')
# # else:
# #     print('비소수')
#
# start = 100000000
# end = 100010000
# cnt = 0
# for i in range(start,end+1):
#     if isPrime(i):
# #        print(i)
#         cnt=+1
#
# def gcd(p,q):
#     pass
#
# a = 105
# b = 30
# G = gcd(a, b)
# L = a*b/G
# print('gcd :', G)
# print('lcm :', L)
#
# def gcd(p,q):
#     if q==0:
#         return p
#     return gcd(q, p%q)

a = 1000000000001
if a%2 ==0:
    print('짝수')
else:
    print('홀수')
if a&1 == 0:
    print("짝수")
else:
    print("홀수")