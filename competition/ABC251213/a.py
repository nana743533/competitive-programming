import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

def main():
    N = II()
    S = input().strip()

    sasikomi = "o" * (N - len(S))

    S = sasikomi + S

    print(S)

if __name__ == "__main__":
    main()


"""
import sys
→ Pythonの標準ライブラリ sys を使えるようにする。
input = sys.stdin.readline
→ 普段の input() の代わりに、標準入力から1行を高速で読む 
sys.stdin.readline() を input という名前で使えるようにしてる。

"""
