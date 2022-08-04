# from itertools import combinations
# import sys
# sys.stdin = open('../files/day3/input1.txt','r')
# ans = 0
# _list = []
# a=input().split()
# b=int(a[0])+1
# c=int(a[1])
# chkP= False
# endP= False
# _if = list(map(int,input().split()))
# for i in range(1,b):
#     _list.append(i)
#
# for i in combinations(_list,c):
#     endP=False
#     newList=list(i)
#     if chkP:
#         for j in range(len(newList)):
#             print(newList[j],end= " ")
#         break;
#
#     if(newList==_if):
#         chkP=True
#         endP=True
# if endP:
#     print('NONE')
#
from itertools import combinations
N,K=map(int,input().split())
key = tuple(map(int,input().split()))
combData = []
for i in combinations(list(range(1, N+1)),K):
    combData.append(i)
idx = combData.index(key)

if key==combData[-1]:
    print('NONE')
else:
    print(' '.join(map(str,combData)))