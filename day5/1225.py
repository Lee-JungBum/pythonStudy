import sys
from collections import deque
sys.stdin = open('../files/day5/input3.txt','r')
ans = 0
dq = deque()

for i in range(1,11):
    a = [] * 8
    la = []
    _ = int(input())
    print('#',i)
    a = input().split()
    dq = deque()
    for j in range (0,8):
        dq.append(a[j])
    j=1
    _out = 3
    while True:
        _in =0
        if _out<=0:
            dq.pop()
            dq.append(0)
            j=1
            break
        _out=int(dq.popleft())-j
        dq.append(_out)
        j+=1
        if j==6:
            j=1

    print('#%d '% i,end='')
    for j in range(0,7):
        print(dq.popleft(),end=' ')
    print(dq.pop())
