n=[]
k=int(input())

for _ in range(k):
    n.append(int(input()))
if(k<4):
    print('Invalid input')
else:
    print(n)
    n.sort()
    print(n)
    a=n[-4:]
    p=1
    for i in range(len(a)):
        p*=a[i]
    print(float(p))
    
