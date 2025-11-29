import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

def cal_next_step(h_max, h_min, t, l, u):
  next_h_max = min(h_max + t, u)
  next_h_min = max(h_min - t, l)
  ok = True
  if (h_max+t > u and h_min-t < l):
    ok = False
  return [next_h_max, next_h_min, ok]

def main():
    T = II()
    for i in range(T):
      N, H = LI()
      print("--------------------------------")
      print(N, H)
      t, l, u = [None] * N, [None] * N, [None] * N
      for j in range(N):
        t[j], l[j], u[j] = LI()
      h_max, h_min = [H, H]
      t.append(0)
      for j in range(0, N):
        h_max, h_min, ok = cal_next_step(h_max, h_min, t[j] - t[j-1], l[j], u[j])
        print(h_max, h_min, ok)
        if ok == False:
          print("No")
          break
        if j == N-1:
          print("Yes")
      


if __name__ == "__main__":
    main()


"""
import sys
→ Pythonの標準ライブラリ sys を使えるようにする。
input = sys.stdin.readline
→ 普段の input() の代わりに、標準入力から1行を高速で読む 
sys.stdin.readline() を input という名前で使えるようにしてる。

"""