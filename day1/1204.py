import sys
sys.stdin = open('../files/input2.txt','r')
ans = 0
cnt = int(input())
for i in range(1,11):
    number = int(input())
    data = list(map(int,input().split()))
    newList = [0]*(max(data)+1)
    for j in range(0,101):
        newList[j] = data.count(j)
    listMax = max(newList)

    ans = list.index(newList,listMax)

    while True:

        try:
            ans = list.index(newList, listMax)
            newList[ans] = 0
        except ValueError:
            break
    print('#%d %d' % (i, ans))