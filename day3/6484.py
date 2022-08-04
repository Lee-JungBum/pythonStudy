# import sys
# import math
#
# sys.stdin = open('../files/day3/input3.txt','r')
# ans = 0
# cnt = int(input())
# count = 0
# for i in range(1,cnt+1):
#     data = list(map(int,input().split()))
#     a=data[0]
#     b=data[1]
#     c= a-b
#     aF=math.factorial(a)
#     bF=math.factorial(b)
#     cF=math.factorial(c)
#
#     num = int(aF/(bF*cF))
#
#     for z in range(1, num + 1):
#         if num % z == 0:
#             count+=1
#
#     print('#%d %d' % (i, count%1000000007))
#     count=0
#### 타임 ? 메모리 에러 발생


# 에라스토테네스체
# a^ab^b => (a+1)(b+1)
import sys

sys.stdin = open('../files/day3/input3.txt', 'r')
maxN = int(1e5)
nums = [0] * maxN
primes = []
for i in range(2, maxN):
    if nums[i]:
        continue
    primes.append(i)
    for j in range(i + i, maxN, i):  # i부터 시작해도 상관없음
        nums[j] = 1
T = int(input()) + 1
for testcase in range(1, T):
    N, K = map(int, input().split())
    ans = 1
    for i in primes:
        if N < i:
            break
        cnt = 1
        tmp = int(N / i)  # N//i
        while tmp:  # 분자
            cnt += tmp
            tmp //= i
        tmp = int((N-K)/i)
        while tmp:  # 분모
            cnt -= tmp
            tmp//=i
        tmp = int(K/ i)
        while tmp:  # 분모
            cnt -= tmp
            tmp //= i
        ans = (ans*cnt)%1000000007
    print('#%d %d' % (testcase,ans))