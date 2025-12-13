import sys
input = sys.stdin.readline

def LI(): return list(map(int, input().split()))
def II(): return int(input())

def main():
  N,  M = LI()
  R = [None] * M
  C = [None] * M

  for i in range (M):
    R[i], C[i] = LI()
  
  RC_tuples = [None] * M
  for i in range(M):
    RC_tuples[i] = (R[i], C[i])
  
  RC_tuples = sorted(RC_tuples, key=lambda RC: RC[0])
  print(RC_tuples)

  for i in range(M-1):
    if (RC_tuples[i][0] == RC_tuples[i+1][0] or RC_tuples[i][0]+1 == RC_tuples[i+1][0]):
      if(RC_tuples[i][1] == RC_tuples[i+1][1] or RC_tuples[i][0]+1 == RC_tuples[i+1][0] or RC_tuples[i][0]-1 == RC_tuples[i+1][0]):
        RC_tuples[i+1]

    else:
      print("No")

if __name__ == "__main__":
    main()
