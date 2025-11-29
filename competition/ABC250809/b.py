S = input()
n = len(S)
Answer= 0

def calper(i,j):
    count = 0
    for k in range(i+1, j):
        if(S[k]=="t"):
            count += 1
    return(count)

for i in range(n-2):
    if(S[i]=="t"):
        for j in range(i+2,n):
            if(S[j]=="t"):
                max(Answer, calper(i,j))

print(Answer)