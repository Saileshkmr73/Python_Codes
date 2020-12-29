n=int(input())
m=[[int(i) for i in input().split()]for j in range(n)]
s=sum(m[i][i]for i in range(n))
s1=sum(m[i][n-i-1]for i in range(n))
print(abs(s-s1))
'''
n=list(map(int,input().rstrip().split()))
p=n[1:]
r=n[0]
for i in p:
    a=[]
    for j in range(r):
        a.append(int(i))
    arr.append(a)
print(arr)
'''
