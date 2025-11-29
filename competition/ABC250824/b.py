import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

n,m = LI()
s = []
for i in range(n):
    s.append(input())
ansl = [0] * n

for j in range(m):
    cnt = 0
    for i in range(n):
        cnt += int((s[i])[j])
    if(cnt == 0 or cnt == n):
        for k in range(n):
            ansl[k] += 1
    elif(cnt <= (n //2)):
        for k in range(n):
            if(s[k][j] == "1"):
                ansl[k] += 1
    else:
        for k in range(n):
            if(s[k][j] == "0"):
                ansl[k] += 1
idxs = [i for i,v in enumerate(ansl) if v == max(ansl)]
for i in idxs:
    print(int(i + 1), end = " ")