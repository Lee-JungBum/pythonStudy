import string
import sys
sys.stdin = open('../files/day2/input1.txt','r')
ans = 0
for i in range(1,11):
    cnt = int(input())
    _if = input()
    data = input()
    print('#%d %s' % (i, data.count(_if)))