import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

def dokomadetaoreru(zahyou, A, A_height, A_max, N):
  a = A_height[zahyou-1]
  #print(zahyou, a, "AAAAAAAAA")
  if a > N:
    return N
  max_tugino = 0
  for i in range(zahyou, a+1):
    max_tugino = max(max_tugino, A_max[i - 1])

  return max_tugino

def main():
  N = II()
  A = LI()
  A_height = []
  for i in range(N):
    A_height.append(A[i] + i)
  A_max = A_height
  for i in range(1, N):
    A_max[i] = max(A_height[i], A_max[i-1])
  #print(A_max)

  a = 1
  while True:
    a = dokomadetaoreru(a, A, A_height, A_max, N)
    if a >= N:
      print(N)
      break
    if a == dokomadetaoreru(a, A, A_height, A_max, N):
      print(a)
      break 




if __name__ == "__main__":
    main()


"""
import sys
→ Pythonの標準ライブラリ sys を使えるようにする。
input = sys.stdin.readline
→ 普段の input() の代わりに、標準入力から1行を高速で読む 
sys.stdin.readline() を input という名前で使えるようにしてる。

"""