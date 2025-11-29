import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

n, q = LI()
a = LI()
b = LI()
c, x, v = [], [], []
for i in range(q):
    iin = list(input().split())
    c.append(iin[0])
    x.append(int(iin[1]))
    v.append(int(iin[2]))

sum = 0
for i in range(n):
    sum += min(a[i], b[i])    #! ans = sum(min(A,B) for A,B in zip(a,b))

for i in range(q):
    m = min(a[x[i] - 1], b[x[i]-1])      #! prev = min(a[X], b[X])
    if(c[i]=="A"):
        a[x[i]-1] = v[i]
        mm = min(a[x[i] - 1], b[x[i]-1]) #! curr = min(a[X], b[X])
        sum -= (m - mm)
    if(c[i]=="B"):
        b[x[i]-1] = v[i]
        mm = min(a[x[i] - 1], b[x[i]-1])
        sum -= (m - mm)
    print(sum)