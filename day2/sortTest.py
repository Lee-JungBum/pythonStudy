# data = [2,3,4,1,5,6,8,7,9,10]
# #default sort : ascending
# print('정렬전 :',data)
# data.sort(reverse=True)
# data2= sorted(data)
# print('정렬후 :',data)
#
#
# data=[[],[],[]]
# data[2,2][1,3],[1,2]
# data(sorted((data)))
#
#                 ]
import sys
sys.stdin = open('../files/day2/input2.txt','r')

cnt = int(input())
ans = list(map(int,input().split()))
B = sum(ans)
print(B)
