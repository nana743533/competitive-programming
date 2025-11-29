import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

def main():
    W,B = LI()
    n = W*1000 // B
    print(n+1)

if __name__ == "__main__":
    main()


"""
import sys
→ Pythonの標準ライブラリ sys を使えるようにする。
input = sys.stdin.readline
→ 普段の input() の代わりに、標準入力から1行を高速で読む 
sys.stdin.readline() を input という名前で使えるようにしてる。

"""