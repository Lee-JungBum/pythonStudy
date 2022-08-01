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


import math
a = 100
b = 3

print(math.pow(a,b))    #무조건 소수
print(a**b) #타입알아서
print(math.sqrt(2))
print(2**0.5) #이것도 루트

ans = a/b
print(ans)
ans = a%b
print(ans)
ans = a//b
print(ans)

print(int(a/b)) #이게제일빠름
print(divmod(a,b))

x02 = 0b100000
x08 = 0o40
x10=32
x16 = 0x20
print(x02,x08,x10,x16)
print(bin(x10))
print(oct(x10))
print(hex(x10))
