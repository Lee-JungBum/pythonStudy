import sys
sys.stdin = open('../files/day1/input.txt', 'r')
ans = 0
for i in range(1,11):
    cnt = int(input())
    data = list(map(int,input().split()))
    for j in range(1,cnt+1):
        _max=max(data)
        indexMax=data.index(_max)
        _min=min(data)
        indexMin=data.index(_min)
        data[indexMax] -= 1
        data[indexMin] += 1
    ans=max(data)-min(data)
    print('#%d %d' % (i,ans))