jw = [0,25,15,10]
jp = [0,20,14,10]
N = 3
w = 30+1
# 보석 무한개
dp1 = [0]*(w+1)
def knap1():
    iLen = w+1
    jLen = N+1
    for i in range(1,iLen): # 가방
        for j in range(1,jLen): # 보석
            if i >= jw[j]:
                if dp1[i] < dp1[i-jw[j]]+jp[j]:
                    dp1[i]= dp1[i-jw[j]]+jp[j]
    return dp1[w]

# 보석 한개
dp2 = [[0]*(w+1) for _ in range(N+1)]
def knap2():
    iLen = N + 1
    jLen = w+1
    for i in range(1,iLen):
        for j in range(1,jLen):
            if jw[i]<=j:
                if dp2[i][j] < dp2[i-1][j-jw[i]]+jp[i]:
                    dp2[i][j] = dp2[i-1][j-jw[i]]+jp[i]
knap1()
print('knap1_2 : %d' % (dp1[w]))
knap2()
print('knap2 : %d' % (dp2[w]))