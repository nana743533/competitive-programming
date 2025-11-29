# template
import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

# 1.1 The First Problem
# 250809
N = int(input())
print(N * N)

# 1.2 Linear Search
# 250809
N, X = map(int, input().split())
A = list(map(int, input().split()))
if (X in A):
    print("Yes")
else:
    print("No")

# 1.3 Two Cards
# 250809
N, K = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
Answer = False

for i in P:
    for j in Q:
        if(i+j==K):
            Answer = True
if(Answer):
    print("Yes")
else:
    print("No")

# 1.4 Binary Representation
# 250809
N = int(input())
ans = []
answer = ""

for i in range(10): 
    ans.insert(0, str(N % 2))  #! 2進法への変換、配列へのinsert()メソッド
    N //= 2
for i in ans:
    answer += str(i)
print(answer)

# 1.5 Three Cards
# 250813
N, K = map(int, input().split())
Answer = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        if(i+j <= K-1 and i+j >= K-N): Answer += 1
print(Answer)

# 2.1 How Many Guests?
# 250817
N, Q = LI()
A = LI()
L, R = [], []                                #! appendじゃなくて[None] * Qでもいい
for i in range(Q):
    hoge = LI()
    L.append(hoge[0])
    R.append(hoge[1])

prefix_sum = [0]
for i in A:
    prefix_sum.append(prefix_sum[-1] + i)     #! 累積和の定番式

for i in range(Q):
    print(prefix_sum[R[i]] - prefix_sum[L[i]-1])  #! 配列の部分和を取るときは、forじゃなくて累積和の引き算

# 2.2 Event Attendance
# 250817
D = II()
N = II()
L, R = [None] * N, [None] * N
li = [0] * (D+1)
for i in range(N):
    L[i], R[i] = LI()
    li[L[i]-1] += 1
    li[R[i]] -= 1
prefix_sum = [0]
for i in li:
    prefix_sum.append(prefix_sum[-1] + i)
for i in range(1,D+1):
    print(prefix_sum[i])

# 2.3 Two Dimensional Sum
# 250817
H, W = LI()
X = [None] * H
for i in range(H):
    X[i] = LI()
Q = II()
ABCD = [None] * Q
for i in range(Q):
    ABCD[i] = LI()

prefix_sum = [[0] * (W+1) for _ in range((H+1))] #! 二次元空配列の作成　同じ配列深いコピー[[0] * W] * Hはダメ
                                                #! 配列の大きさを1つ大きくしている 
for i in range(H):
    for j in range(W):
        prefix_sum[i][j] = X[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
#! 横に累積和→縦に累積和が定石

for i in ABCD:
    a,b,c,d = i
    print(prefix_sum[c-1][d-1] - prefix_sum[c-1][b-2] - prefix_sum[a-2][d-1] + prefix_sum[a-2][b-2])

# 2.4 Winter in ALGO Kingdom
# 250818
H, W, N = LI()
ABCD = []
for i in range(N):
    ABCD.append(LI())
Z = [[0]*(W+2) for i in range((H+2))]

for i in range(N):                   #! 枠の左上内側に点を打つ方が普通
    a,b,c,d = ABCD[i]
    Z[c-1][d-1] += 1
    Z[c-1][b-2] -= 1
    Z[a-2][d-1] -= 1
    Z[a-2][b-2] += 1

for i in reversed(range(H)):          #! 二次元配列の累積和の定石
    for j in range(W):
        Z[i][j] += Z[i+1][j]
for i in reversed(range(W)):
    for j in range(H):
        Z[j][i] += Z[j][i+1]

for i in range(H):
    for j in range(W):
        print(Z[i][j], end=" ")       #! 二次元配列の出力
    print("")

# 2.5 Resort Hotel
# 250824
N = II()
A = LI()
D = II()
L, R = [0]*D, [0]*D
for i in range(D):
    L[i], R[i] = LI()
prefix_max = [0]*N
prefix_max_revert = [0]*N
prefix_max[0] = A[0]
prefix_max_revert[0] = A[-1]

for i in range(1, N):
    prefix_max[i] = max(prefix_max[i-1], A[i])                     #! prefix_max or min への応用
    prefix_max_revert[i] = max(prefix_max_revert[i-1], A[N-i-1])

for i in range(D):
    a = prefix_max[L[i]-2]
    b = prefix_max_revert[N - (R[i]) -1]
    print(max(a,b))

