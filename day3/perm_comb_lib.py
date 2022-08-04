from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement as cwr

data = ['a','b','c']
# 순열 nPr= n*(n-1)_*n(n-2).....+n*(n-r+1)
# =n! / (n-r)!
print("순열")
for i in permutations(data,2):
    print(i)
print("중복순열")
for i in product(data,repeat=2):
    print(i)
# nCr = nPr/r! = nPr / ((r-1))!*r!/
print("조합")
for i in combinations(data,2):
    print(i)
# nHr = n+r-1 C r,
print("중복조합")
for i in cwr(data,2):
    print(i)