import sys
sys.stdin = open('../files/day1/input.txt', 'r')

# _str = input()

# cnt, *data = _str.split()
# print(cnt,data)
# idata = []
# for i in data:
#     idata.append(int(i))
#
# print(idata)

# iData = [range(1,11)]
# print(iData)
# iData = list(range(1,11))
# print(iData)

# cnt,*data = list(map(int,input().split()))
# print(cnt,data)

# a = 100
# b = 200
# print(a, b)
# for i in range(1, 6):
#     print(i, end=" ")
# print()
# print('end')

# tc = 1
# ans = 100
# print('#%d %d' % (tc,ans))
# print('#{} {}'.format(tc,ans))

arr1 = [0]*10
arr1 = [i for i in range(1,11)] #콩그레이션

# arr2 = [[0]*5]*5
# print(arr2)
#
# arr2[0][0]=100
# for i in range(0,5):
#     for j in range(0,5):
#         print(arr2[i][j],end=' ')
#     print()

arr2 = list(0 for _ in range(5))
print(arr2)
arr2 = [[0]*5 for _ in range(5)]
arr2[0][0]=100
# print(arr2)
for i in arr2:
    for j in i:
        print(j,end=' ')
    print()