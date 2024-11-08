import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

cnt = 0
start, end = 0, 0
current_sum = 0

while end <= N:
    if current_sum == M:
        cnt += 1
        current_sum -= numbers[start]
        start += 1
    elif current_sum < M:
        if end == N:
            break
        current_sum += numbers[end]
        end += 1
    else:  # current_sum > M
        current_sum -= numbers[start]
        start += 1

print(cnt)
