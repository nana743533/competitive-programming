N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = sum(min(a, b) for a, b in zip(A, B))        #! 内包表記　リストの小さい方の和

for _ in range(Q):
    c, X, V = input().split()
    X, V = int(X) - 1, int(V)

    prev = min(A[X], B[X])

    if c == "A":
        A[X] = V
    else:
        B[X] = V

    curr = min(A[X], B[X])
    ans = ans - prev + curr

    print(ans)
