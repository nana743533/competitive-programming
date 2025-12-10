import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

def main():
  # 入力
  N, M = LI()
  X = [None] * M
  Y = [None] * M
  for i in range(M):
    X[i], Y[i] =LI()
  Q = II()
  quety = [None] * Q
  for i in range(Q):
    quety[i] = LI()

  # 頂点定義
  vertex = [None] * N
  for i in range(N):
    vertex[i] = [i+1, 0]  # 頂点v, color

  # 幅優先探索
  def bfs(v):
    for i in range(M):
      vv = []
      if X[i] == v:
        vv.append(Y[i])
    return(vv)

  
  # クエリの処理
  for i in range(Q):
    if quety[i][0] == 1:
      vertex[quety[i][1]][1] = 1 # colorを黒に変更
    else: # 頂点vから変を辿って黒色にtどりつけるかを判定
     v = quety[i][1]
     
      

    

if __name__ == "__main__":
    main()


"""
import sys
→ Pythonの標準ライブラリ sys を使えるようにする。
input = sys.stdin.readline
→ 普段の input() の代わりに、標準入力から1行を高速で読む 
sys.stdin.readline() を input という名前で使えるようにしてる。



"""



