N, Q = map(int, input().split())
A = list(map(int,input().split()))
B = []
for i in range(Q):
    B.append(int(input()))

def returnx (b):
    if(b >= max(A)+1): return -1

    lucky = 0
    for a in A:
        if(a <= b-1): lucky += (b-a)
    
    return((b-1)*N + 2 - lucky)

for i in B:
    print(returnx(i))