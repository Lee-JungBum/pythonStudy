# 순차검색 , O(n)
data = [3, 2, 4, 6, 7, 9, 10, 5, 1]

key = 8
flag = False
cnt = 0
for i in data:
    cnt += 1
    if i == key:
        flag = True
        break

if flag:
    print('Y')
else:
    print('N')

print("cnt : ", cnt)
