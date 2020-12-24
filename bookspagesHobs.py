n=int(input())
p=int(input())
count=0
count_bck=0


for i in range(1,n+1,2):
    if(i>=p):
        break
    else:
        count+=1
for i in range(n,0,-2):
    if(i<=p):
        break
    else:
        count_bck+=1

print(min(count,count_bck))


'''
n = int(input())
p = int(input())
print(min(p//2, n//2 - p//2))
'''

