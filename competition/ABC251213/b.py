import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())





def main():

  def kakikomi (pos, number, ban, N):
    for i in range(0, N):

      ban[pos[0]][pos[1]] = number + i

      if i == N-1:
        break

      pos[0] -= 1
      pos[1] += 1

      if pos[0] == -1 : pos[0] = N-1
      if pos[1] == N : pos[1] = 0


  N = II()

  ban = [[0] * N for _ in range(N)]

  pos = [0, (N - 1) // 2]
  number = 1

  for _ in range(N):
    kakikomi(pos, number, ban, N)
    number += N
    if pos[0] != N-1:
      pos[0] += 1
    else:
      pos[0] = 0

  for row in ban:
    print(*row)

    
if __name__ == "__main__":
    main()



"""
import sys
→ Pythonの標準ライブラリ sys を使えるようにする。
input = sys.stdin.readline
→ 普段の input() の代わりに、標準入力から1行を高速で読む 
sys.stdin.readline() を input という名前で使えるようにしてる。

"""
