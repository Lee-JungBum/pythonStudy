import sys
sys.stdin = open('../files/day5/input1.txt','r')
T=11
def priority(op):
    if op == '+' or op =='-':
        return 1
    elif op == '*' or '/':
        return 2
    else:
        return 3
for testCase in range(1,11):
    input()
    data = input()
    stk = []
    postStr = []
    for i in data:
        if i < '0':
            if i == '(':
                stk.append(i)
            elif i == ')':
                peek = stk[-1]
                while peek!='(':
                    postStr.append(stk.pop())
                    peek = stk[-1]
                stk.pop()
            else:
                if stk:
                    peek = stk[-1]
                    while priority(i) >priority(peek):
                        postStr.append(stk.pop())
                        peek = stk[-1]
                stk.append(i)
        else:
            postStr.append(i)
    while stk:
        postStr.append(stk.pop())
    for i in postStr:
        if i <'0':
            a=stk.pop()
            b=stk.pop()
            if i =='+':
                stk.append(b+a)
            elif i =='*':
                stk.append(a*b)
        else:
            stk.append(int(i))


    print('#%d %d' % (testCase, stk.pop()))
