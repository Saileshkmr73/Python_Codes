'''
1 to N - Mixed Pattern Printing
The program must accept a number N and print the numbers from 1 to N with
he first number being 1, second number being N, third being 2 and the 
fourth being N-1 and so on.
Input Format:
The first line contains N.
Output Format:
The first line contains the values from 1 to N arranged in the format described above.
Boundary Conditions:
1 <= N <= 500
Example Input/Output 1:
Input:
9
Output:
1 9 2 8 3 7 4 6 5
Example Input/Output 2:
Input:
6
Output:
1 6 2 5 3 4

#method1:
n=int(input())
c=[]
for k in range(1,n+1):
    c.append(k)
b=c[::-1]
d=[]
for l in range(n//2+1):
    d.append(str(c[l]))
    d.append(str(b[l]))
print(' '.join(d[:n]))
'''
#method2
n=int(input())
m=list(range(1,n//2+2))
b=list(range(n//2+2,n+1))
b=b[::-1]
for i in range(len(m)):
    print(m[i],end=" ")
    try:
        print(b[i],end=" ")
    except:
        continue
