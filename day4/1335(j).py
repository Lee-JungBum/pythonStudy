import sys

sys.stdin = open('../files/day4/input2.txt')
N = int(input())
mapData = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0


def check(y, x, n):
    global white
    global blue
    temp = mapData[y][x]
    flag = True
    for i in range(y,n+y):
        for j in range(x,n+x):
            if temp != mapData[i][j]:
                flag = False
                break
        if not flag:
            break
    if flag:
        if temp:
            blue += 1
        else:
            white += 1
    else:
        check(y, x, n // 2)  # 위/ 왼
        check(y, x + n // 2, n // 2)  # 위 / 오
        check(y + n // 2, x, n // 2)  # 아 / 왼
        check(y + n // 2, x + n // 2, n // 2)  # 아 / 오





check(0, 0, N)
print(white)
print(blue)
