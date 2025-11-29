# test execute
import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

n,k = LI()
a = LI()

def maisuu(sec):
	mai = 0
	for i in a:
		mai += sec // i
	return mai
print(maisuu(6))

l = 0
r = min(a) * k
while l < r:
    m = (r + l) // 2
    print(m,l,r)
    if(k < maisuu(m)):
        r = m
        break
    elif(k == maisuu(m)):
        print(m)
        break
    else:
        l = m