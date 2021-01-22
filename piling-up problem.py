for t in range(int(input())):
    input()
    lst = list(map(int,input().split()))
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    if (i == l - 1):
        print('Yes') 
    else:
        print('No')

'''
2
6
4 3 2 1 3 4
3
1 3 2
Teest cases:
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n  space separated integers, denoting the sideLengths of each cube in that order.

Constraints



Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input

2
6
4 3 2 1 3 4
3
1 3 2

Sample Output

Yes
No
Explanation

In the first test case, pick in this order: left - 4, right -4 , left -3 , right - 3, left -2 , right -1 .
In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.