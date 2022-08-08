import sys
sys.stdin = open('../files/day6/input1.txt')

left = [-1]*100
right= [-1]*100

for testCase in range(1,2):
    _,cnt = map(int,input().split())
    data = list(map(int,input().split()))
    for i in range(cnt):
        if left[data[i]] == -1
