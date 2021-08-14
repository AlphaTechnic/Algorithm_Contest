import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline


def solution(numOfStairs):
    dp = [0 for _ in range(75)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[4] = 7
    for i in range(5, 71):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    return dp[numOfStairs]


if __name__ == "__main__":
    print(solution(6))