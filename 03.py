# template
import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

# 3.1 Binary Search 1
# 250824
n,x = LI()
a = LI()
def search(x, A):
	L = 0
	R = n-1
	while L <= R:
		M = (L + R) // 2
		if x < A[M]:
			R = M - 1
		if x == A[M]:
			return M
		if x > A[M]:
			L = M + 1
	return -1 # 整数 x が存在しない（注：この問題の制約で -1 が返されることはない）
print(search(x,a) + 1)
'''                         #! bisect(ソート配列,値)を使う 
import bisect
print(bisect.bisect_left(a,x) + 1)
'''

# 3.2 printer
# 250824
n,k = LI()
a = LI()

def maisuu(sec):
	mai = 0
	for i in a:
		mai += sec // i
	return mai

l = 0
r = min(a) * k
while l < r:
    m = (r + l) // 2
    if(k < maisuu(m)):
        r = m
    elif(k == maisuu(m)):
        print(m)
        break
    else:
        l= m