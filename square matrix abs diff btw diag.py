n=int(input())
arr=[]
for _ in range(n):
        arr.append(list(map(int,input().rstrip().split())))
print(arr)
dia1=0
dia2=0
for i in range(len(arr)):
    dia1+=arr[i][i]
    dia2+=arr[i][n-i-1]
print(abs(dia1-dia2))
