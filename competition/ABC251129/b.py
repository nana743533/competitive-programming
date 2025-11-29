import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

def main():
    N, M = LI()
    A, B = [None] * N, [None] * N
    for i in range(N):
        A[i], B[i] = LI()
    for k in range(M):
      k += 1
      sum_k = 0
      cnt = 0
      for i in range(N):
        if(A[i]==k):
          sum_k += B[i]
          cnt +=1
      if(cnt == 0):
        print(0)
      else:
        avg = sum_k / cnt
        print(avg)
        


if __name__ == "__main__":
    main()
