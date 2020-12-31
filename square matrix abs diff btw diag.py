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


'''
n=int(input())
m=[[int(i) for i in input().split()]for j in range(n)]
s=sum(m[i][i]for i in range(n))
s1=sum(m[i][n-i-1]for i in range(n))
print(abs(s-s1))
'''
'''
mat = [[int(input()) for x in range (C)] for y in range(R)] 
to take input on each line
'''
