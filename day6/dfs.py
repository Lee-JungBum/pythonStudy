import sys
sys.stdin = open("../files/day6/input.txt",'r')
V,E = map(int,input().split())
g = [[0]*(V+1) for _ in range(V+1)]
def dfs1():

for i in range(E):
    sn, en =map(int,input().split())
    g[sn][en] = 1
    g[en][sn] = 1
# for i in g:
#     for j in i:
#         print(j,end=' ')
#     print()

visited = [0]*(V+1)
stk = []
start = 1
stk.append(start)
visited[start] = 1
print('bfs1 : [',end = ' ')
while stk:
    n = stk.pop()
    print(n,' ',end = ' ')