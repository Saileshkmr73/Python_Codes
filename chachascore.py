size=int(input())
b=list(map(int,input().split()))
a=b[0:size]
size_c=int(input())
cha=list(map(int,input().split()))
j=cha[0:size_c]

n=sorted(set(a),reverse=True)

c=[]
for i in j:
    if(i<min(n)):
            c.append(len(n)+1)
    for k in n:
        if(i>=k):
            c.append(n.index(k)+1)
            break
print('\n'.join(map(str, c)))
           

'''
Problem Statement:-  Chacha is playing an arcade game and wants to climb to the top of the leader board and wants to track her ranking. The game uses Dense Ranking so its leader board works like this:

The player with the highest score is ranked number 1 on the leader board.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
For example, the four players on the leader board have high scores of 100, 90, 90, and 80. Those players will have ranks 1, 2, 2, and 3, respectively. If Chacha’s scores are 70, 80 and 105, her rankings after each game are 4th, 3rd and 1st.

Function Description

Write a function climbing. It should return an integer array where each element res[j] represents Chacha’s rank after the j game.

climbing has the following parameter(s):

scores: an array of integers that represent leaderboard scores
alice: an array of integers that represent Chacha’s scores
Input Format

The first line contains an integer n, the number of players on the leaderboard.
The next line contains n space-separated integers scores[i], the leaderboard scores in decreasing order.
The next line contains an integer, m, denoting the number games Chacha plays.
The last line contains m space-separated integers chacha[j], the game scores.
 

Sample Input

      7

      100 100 50 40 40 20 10

      4

      5 25 50 120

Sample Output

      6

      4

      2

      1
'''
