# import sys
# sys.stdin = open('../files/day2/input3.txt','r')
# ans = 0
# for z in range(1,11):
#     _ = int(input())
#     rowData = [input() for _ in range(100)]
#     ColData = [''.join(x) for x in zip(*rowData)]
#     chk=True
#     maxLen = 0
#     for _len in range(100,1,-1): # 문자열의 길이
#         for words in rowData: # 각각의 열의 문자열
#             for i in range(100-_len+1): # 경우의 수
#                 chk=True
#                 for j in range(int(_len/2)): # 검증
#                 # == for j in range(_len//2) 위에께 더빠름
#                     if rowData[i+j] != rowData[_len+i-j-1]:
#                         chk = False
#                         break
#                 if chk:
#                     break
#             if chk:
#                 if maxLen < _len:
#                     maxLen=_len
#                 break
#         if chk:
#             break
#     print('#%d %d' % (z, maxLen))
#     #print('#%d %d' % (z, _len))

_str = 'abcbade'
_str2 = _str[0:5]
_str3 = _str[4::-1]
print(_str2)
print(_str3)

#미완