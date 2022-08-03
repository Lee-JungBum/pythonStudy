def selectSort(n):
    for i in range(n - 1):
        maxIdx = 0
        for j in range(1, n - i):
            if data[maxIdx] < data[j]:
                maxIdx = j
        data[n - 1-i], data[maxIdx] = data[maxIdx], data[n - 1-i]

def mergeSort(s,e):
    if s<e:
        m= (int(s+e)/2)
        mergeSort(s,m)
        mergeSort(m+1,e)

        p=s
        q=m+1
        idx=s
        while p<=m or q<=e:
            if q>e or  (p<=m and data[p]<data[q]):
                temp[idx] = data[p]
                idx+=1
                p+=1
            else:
                temp[idx] = data[q]
                idx+=1
                q+=1

            for i in range(s,e+1):
                data[i] = temp[i]

searchCnt = 0
def binarySearch(s,e,key):
    global searchCnt
    while s<=e:
        searchCnt +=1
        m = int((s+e)/2)
        if data[m] < key:
            s = m+1
        elif data[m] >key:
            e = m-1
        else:
            return m
    return -1
def binarySearch2(s,e,key):
    global searchCnt
    while s<=e:
        searchCnt +=1
        m = int((s+e)/2)
        if data[m] < key:
            s = m+1
        elif data[m] >key:
            e = m-1
        else:
            return m
    if data[s] < key:
        return s+1
    else:
        return s
n = 10
data = [1, 2, 11, 3, 5, 6, 8, 7, 9, 10]
temp = [0]*len(data)
print("정렬전 :", data)
selectSort(n)
# mergeSort(0,n-1)
print("정렬후 :", data)
#
# key=11
# idx = binarySearch(0,n-1,key)
# print('idx :',idx)
# print('sCnt :',searchCnt)
key=4
#LIS
idx = binarySearch2(0,n-1,key)
print("idx :",idx)