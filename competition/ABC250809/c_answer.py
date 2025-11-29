import sys
input = sys.stdin.readline                       #! 入力処理テンプレート
import bisect

def LI(): return list(map(int, input().split())) #!
def II(): return int(input())                    #! 

def main():
    N, Q = LI()
    A = LI()
    A.sort()                                     #! 配列へのsort()メソッド

    prefix_sum = [0]
    for v in A:
        prefix_sum.append(prefix_sum[-1] + v)    #! append()で累積和(prefix_sum)を追加

    max_A = A[-1]                                #! ソート配列から最大値を所得

    for _ in range(Q):
        B = II()
        if B > max_A:
            print(-1)
            continue
        idx = bisect.bisect_left(A, B)               #! bisect(ソート配列,値)でインデックス所得 
        cnt = prefix_sum[idx] + (B - 1) * (N - idx)
        print(cnt + 1)

if __name__ == "__main__":
    main()
