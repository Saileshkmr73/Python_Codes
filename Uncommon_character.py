n=int(input())
k=[]
for _ in range(n):
    k.append(*input().split())
common=[]
for i in k[0]:
    cnt=0
    for j in range(1,n):
        if i in k[j]:
            cnt+=1
    if(cnt==n-1):
        common.append(i)
ct=0
for i in k:
    maxi=0
    for j in i:
        if j not in common:
            maxi+=1
    if(maxi>ct):
        ct=maxi
        string=i
print(string)
        
        
            
    
'''

Maximum Uncommon Characters: Given N strings as input, the program must print the string which has the maximum number of uncommon characters. If more than one strings have the same number of uncommon characters print the first occurring string.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains the value of N.
The N lines contain a string each.

Output Format:
The first line contains a string.

Example Input/Output 1:
Input:
4
tiger
umbrella
power
killer

output:
umbrella

Explanation:
The common characters are e and r.
The uncommon characters are (t i g), (u m b l l a), (p o w), (k i l l).
Hence umbrella is the output.

Example Input/Output 2:
Input:
3
aaayz
yzbcd
cceyz

output:
aaayz

Explanation:
The common characters are y and z.
The uncommon characters are (a a a), (b c d), (c c e).
Hence aaayz is the output.
'''
