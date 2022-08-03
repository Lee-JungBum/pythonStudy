import sys

sys.stdin = open('../files/day2/input2.txt', 'r')
ans = 0
for _ in range(1, 11):
    cnt = int(input())
    ansX = [0] * 100
    ansY = [0] * 100
    ansZ = [0] * 2
    tmp = [0] * 3
    data = [[0] * 100 for _ in range(100)]
    for i in range(100):
        data[i] = list(map(int, input().split()))
    for i in range(100):
        for j in range(100):
            ansX[i] += data[i][j]
            ansY[i] += data[j][i]
        ansZ[0] = data[i][i]
        ansZ[1] = data[99 - i][99 - i]
    tmp[0] = max(ansX)
    tmp[1] = max(ansY)
    tmp[2] = max(ansZ)
    print('#%d %d' % (_, max(tmp)))
