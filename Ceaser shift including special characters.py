n=input()
key=int(input())
res=''
for i in n:
    res+=chr((ord(i)+key-32)%94 + 32)
print(res)

Char(mod((V(i)+n-32),94)+32)
