import sys
#수정해야함
sys.stdin = open('../files/day4/input3.txt')

# 탐욕 알고리즘
M, S, C = map(int, input().split())
rooms = []
minus = []
for _ in range(C):
    rooms.append(int(input()))

if M < C:
    rooms.sort()
    for i in range(1):
        minus.append((rooms[i] - rooms[i - 1] - 1))
    minus.sort()
    ans = rooms[-1] - rooms[0] + 1
    for j in range(-1, -M, -1):
        ans -= minus[j]
    print(ans)
else:
    print(C)
