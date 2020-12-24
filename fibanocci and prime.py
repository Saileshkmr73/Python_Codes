'''n=int(input())
n1=0
n2=1
#1,1,2,3,5,8,13,21,34
count=0
if(n==1):
    print(n)
else:
    while(count<n):
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
    print(n1)'''

'''prime'''
p=int(input())
for i in range(2,p):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i)