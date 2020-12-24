if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s=0
    for i in student_marks[query_name]:
        s+=i
    s=s/len(student_marks[query_name])
    print('{:.2f}'.format(s))



Sample Test Cases:

Input (stdin)

Download
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Expected Output

Download
56.00

Success
Input (stdin)

Download
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Expected Output

Download
26.50