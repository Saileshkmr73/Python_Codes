def fibbo(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
       print("Please enter a positive integer")
    elif n == 1:
       print(n)
    else:
        while count < n:
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
        print(n1)

def prime(n):
    count = 0
    for i in range(2, 99999):
        flag=0
        for j in range(2,i):
            if (i % j == 0):
                flag=1
                break
        if flag == 0:
            count+=1
            if count == n:
                print(i)
                break
 
# main
n = int(input())
if n%2 == 1:
    fibbo(n//2+1)
else:
    prime(n//2)




'''
Problem
1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, ……..
This series is a mixture of 2 series – all the odd terms in this series form a Fibonacci series and all the even terms are the prime numbers in ascending order.

Write a program to find the Nth term in this series.

The value N is a Positive integer that should be read from STDIN.
The Nth term that is calculated by the program should be written to STDOUT.
Other than the value of Nth term, no other characters/strings or message should be written to STDOUT.
For example, when N = 14, the 14th term in the series is 17. So only the value 17 should be printed to STDOUT.
'''