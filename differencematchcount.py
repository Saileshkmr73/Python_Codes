num=list(map(int,input().split()))
n=num[0]
dif=num[1]
st=list(map(int,input().split()))
count=0
j=len(st)-1
for i in range(len(st)):
    if(st[i]!=st[j]):
        a=abs(st[i]-st[i+1])        
        if(a==dif):
            count+=1
print(count)

'''
Problem Statement:-   You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.

For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: 2-1 = 1, 3-2 = 1, and 4-3 = 1.

Function Description

Write a function pairs. It must return an integer representing the number of element pairs having the required difference.

pairs has the following parameter(s):

k: an integer, the target difference
arr: an array of integers
Input Format

The first line contains two space-separated integers n and k, the size of arr and the target value.
The second line contains n space-separated integers of the array arr.
Sample Input

     5 2

     1 5 3 4 2 

Sample Output

     2
'''
        
