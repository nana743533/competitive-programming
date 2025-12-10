import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

def main():
  N = II()
  A = LI()
  
  ans = 0
  for l in range(1,N+1):
    for r in range(l,N+1):
      cnt = 0
      for i in range(l,r+1):
        cnt += A[i-1]
      for i in range(l,r+1):
        if (cnt % A[i-1] == 0):
          break
        if (i == r):
          ans += 1
  print(ans)



if __name__ == "__main__":
    main()


"""
import sys
→ Pythonの標準ライブラリ sys を使えるようにする。
input = sys.stdin.readline
→ 普段の input() の代わりに、標準入力から1行を高速で読む 
sys.stdin.readline() を input という名前で使えるようにしてる。

"""