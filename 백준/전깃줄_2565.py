'''
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

3
----------
1 8
2 2
3 9
4 1
6 4
7 6
9 7
10 10

1 8과 2 2는 서로 공존 불가하므로 1
1 8, 2 2는 1이고 1 8 또는 2 2는 3 9와 공존 가능하고 1 8과 2 2 중 연결 가능한 최대 수가 둘 다 1이므로 1 + 1
1 8, 2 2, 3 9는 4 1과 모두 서로 공존 불가하므로 1
1 8, 2 2, 3 9, 4 1 중 2 2 또는 4 1은 6 4와 공존 가능하고 2 2와 4 1 중 연결 가능한 최대 수가 둘 다 1이므로 1 + 1
1 8, 2 2, 3 9, 4 1, 6 4 중 2 2, 4 1, 6 4은 7 6과 공존 가능하고 연결 가능한 최대 수는 2(6 4)이므로 2 + 1
1 8, 2 2, 3 9, 4 1, 6 4, 7 6 중 1 8, 2 2, 4 1, 6 4, 7 6은 9 7과 공존 가능하고 연결 가능한 최대 수는 3(7 6)이므로 3 + 1
1 8, 2 2, 3 9, 4 1, 6 4, 7 6, 9 7 중 1 8, 2 2, 3 9, 4 1, 6 4, 7 6, 9 7은 10 10과 공존 가능한고 연결 가능한 최대 수는 4(9 7)이므로 4 + 1

주어진 전체 연결 개수(n)에서 공존 가능한 최대 개수를 빼면 제거해야 할 개수가 나옴
'''

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()

dp = [1] * n

for i in range(n):
    for j in range(i):
        if (lines[i][1] > lines[j][1]) and (dp[i] < dp[j] + 1):
            dp[i] = dp[j] + 1

print(lines, dp)
print(n - max(dp))
