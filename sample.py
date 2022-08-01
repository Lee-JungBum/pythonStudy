import sys
sys.stdin = open('../files/input.txt','r')
ans = 0
for i in range(1,11):
    cnt = int(input())
    data = list(map(int,input().split()))
    print('#%d %d' % (i, ans))