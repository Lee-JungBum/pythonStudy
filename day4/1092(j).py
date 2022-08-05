a,b = map(int,input().split())
a%=20091024
base=b
tmp = 2
i=2
j=2
ans = a
cnt=0;2
tmp =0
ttmp=1
tr= b
#2 4
while True:
    ans = ans * ans

    if tr==1:
        ttmp= a*b

        break
    if i > b:# 32 31
        if(b==1):
            ttmp*=base
            break
        if(a==2 and b%2==1):
            tmp*=2
            ttmp=tmp
            break
        i/=2

        b=b-i
        i=2
        ans = a*a
        ttmp=ttmp*tmp
        if b==0:
            break
    i *= 2
    tmp=ans
print(ttmp%20091024)









#
# mod = 20091024
# X,Y = map(int,input().split())
# X%=mod
# ans =1
# while Y:
#     if Y&1:
#         ans = ans*X
#     X= (X*X)%mod
#     Y = Y >>1