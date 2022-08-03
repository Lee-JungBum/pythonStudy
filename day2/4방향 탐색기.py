#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]
cx = 2
cy = 3
for i in range (0,4):
    nx = cx + dx[i]
    ny = cy + dy[i]
    print('nx : ', nx, 'ny : ',ny)