import sys
sys.stdin = open('../files/day5/input2.txt','r')
ans = 0
for _ in range(1,11):
    cnt,a = input().split()
    cnt=int(cnt)
    la=[]
    for i in range(0,cnt):
        la= list(map(int,str(a)))
    i=2
    while True:
        if i==cnt:
            break
        if la[i]==la[i-1]:
            la.pop(i)
            la.pop(i-1)
            i = 0
            cnt -= 2

        i+=1

    print('#%d %s' % (_, ''.join(map(str,la))))

