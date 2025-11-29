N, Q = map(int, input().split())
A = list(map(int,input().split()))
B = []
for i in range(Q):
    B.append(int(input()))
A.sort()
archive = []
for i in range(1,101):
    archive.append(sum(A[:1000*i]))

def returnx (b):
    if(b >= max(A)+1): return -1

    lucky = 0
    idx = 0
    start = 0
    for a in A:
        if(a <= b-1): idx += 1
        else: break
    if(idx > 1000): 
        lucky += archive[(idx//1000)-1]
        start = (idx//1000)*1000
    for a in range:
        if(a <= b-1): lucky += (b-1-a)
        else: break
    
    return((b-1)*N + 1 - lucky)

for i in B:
    print(returnx(i))