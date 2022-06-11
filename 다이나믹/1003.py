




# https://www.acmicpc.net/problem/1003

n = int(input())

zero_dp = [1, 0, 1]

one_dp = [0, 1, 1]


def fibo(x):
    if len(zero_dp) <= x:
        for i in range(len(zero_dp), x + 1):
            zero_dp.append(zero_dp[i - 1] + zero_dp[i - 2])
            one_dp.append(one_dp[i - 1] + one_dp[i - 2])


for _ in range(n):
    num = int(input())
    fibo(num)
    print(zero_dp[num], one_dp[num])