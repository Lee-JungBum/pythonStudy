moneys = [0, 1, 4, 5, 10, 40, 50, 100, 400, 500]
MONEY = 800
N = 9
dp = [0] * (MONEY + 1)  # 보석 한개

maxx=987654321;
def getCnt():
    iLen = MONEY + 1
    jLen = N + 1

    for i in range(1, iLen):
        dp[i] = 987654321  # INF
    for i in range(1, iLen):
        for j in range(1, jLen):
            if i >= moneys[j]:
                if dp[i] < dp[i - moneys[j]] + 1:
                    dp[i] = dp[i - moneys[j]] + 1


getCnt()
print('money min : %d' % (dp[MONEY]-maxx))
