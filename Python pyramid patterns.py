for i in range(5,1,-1):
    for j in range(0,i-1):
        print('*',end=" ")
    print("\n")
output:
*  *  *  *  

*  *  *  

*  *  

* 


for i in range(0,5):
    for j in range(0,i+1):
        print('* ',end=" ")
    print("\n")

output:
*  

*  *  

*  *  *  

*  *  *  *  

*  *  *  *  * 





def print_rangoli(size):
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = myStr[size:x:-1]+myStr[x:size]
        print ("--"*x+'-'.join(line)+"--"*x)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
	
	
	
output:

Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------


#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------







num=5
for i in range(0,num):
    for k in range(num-i+1,1,-1):
        print(' ',end="")
    for l in range(0,i+1):
        print('* ',end="")
    print()
for i in range(0,num):
    for l in range(0,i+1):
        print(' ',end="")
    for k in range(num-i+1,1,-1):
        print("* ",end="")
    print()


output:

    * 
   * * 
  * * * 
 * * * * 
* * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

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

output:
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 



num=3
for i in range(0,num):
    c='A'
    for k in range(num-i,0,-1):
        print(' ',end="")
    for l in range(0,i+1):
        print(c,end="")
        c=chr((ord(c)+1-65)%26+65)
    print()

output:
   A
  AB
 ABC