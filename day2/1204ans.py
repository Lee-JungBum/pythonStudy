import sys
sys.stdin = open('../files/input.txt','r')
tc = int(input())+1

for testCase in range(1,tc):
    _=input()
    nums = list(map(int,input().split()))
    cnts = [0]*101
    for i in nums:
        cnts[i]+=1
    maxV= max(nums)
    maxIdx = cnts.index(maxV)
    for i in range(maxIdx,101):
        if(cnts[maxIdx]<=cnts[i]):
            maxIdx=i

    print('#%d %d' % (i, maxIdx))