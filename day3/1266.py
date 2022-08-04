# 1-A실패-B실패
# 1-(1-A성공확률)*(1-B성공확률)
import sys

sys.stdin = open('../files/day3/input2.txt', 'r')
primes = [2, 3, 5, 7, 11, 13, 17]
dpMemo = [[0] * 19 for _ in range(19)]


def set(n, r):
    if r == 0 or r == n:
        return 1
    if dpMemo[n][r] == 0:
        dpMemo[n][r] = set(n - 1, r - 1) + set(n - 1, r)
    return dpMemo[n][r]


for i in primes:
    set(18, i)
T = int(input()) + 1
for testCase in range(1, T):
    pA, pB = map(int, input().split())
    pA /= 100
    pB /= 100

    sA = 0.0
    sB = 0.0
    for i in primes:
        sA += dpMemo[18][i] * (pA ** i) * ((1 - pA) ** (18 - i))
        sB += dpMemo[18][i] * (pB ** i) * ((1 - pB) ** (18 - i))
    print('#%d %.6f' % (testCase, 1 - (1 - sA) * (1 - sB)))
