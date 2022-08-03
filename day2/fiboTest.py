# fibo 초기값 2개 선언 , 0 : 0, 1 : 1 f(n) = f(n-1_+f(n-2_ n>1
reCnt =0
def fibo(n):
    global reCnt
    reCnt+=1
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

idxNum = 30
print('fibo({}) ={}'.format(idxNum,fibo(idxNum)))
print('reCnt :',reCnt)