num=5
for i in range(0,num):
    for k in range(num-i,1,-1):
        print(' ',end="")
    for l in range(0,i+1):
        print('* ',end="")
    print()
for i in range(0,num):
    for l in range(0,i+1):
        print(' ',end="")
    for k in range(num-i,1,-1):
        print("* ",end="")
    print()
