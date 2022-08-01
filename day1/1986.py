import sys
sys.stdin = open('../files/input3.txt','r')
ans = 0
cnt = int(input())
for i in range(1,cnt+1):
    num= int(input())
    a=1
    ans=0
    for j in range(1,num+1):
        if j%2==0:

            ans-=a
            a += 1
        else:
            ans+=a
            a+=1
    print('#%d %d' % (i, ans))