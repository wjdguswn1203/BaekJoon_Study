def padovan_sequence(max_n):
    # 최대값까지의 dp 배열을 준비하고, 초기값 설정
    dp = [0] * (max_n + 1)
    dp[1], dp[2], dp[3] = 1, 1, 1
    
    # 점화식을 이용하여 수열을 계산
    for i in range(4, max_n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    
    return dp

# 테스트 케이스 수 입력
T = int(input())
n = []
for _ in range(T):
    n.append(int(input()))

# 입력된 모든 n 중 최대값을 구해서, 한 번만 dp를 계산
max_n = max(n)
dp = padovan_sequence(max_n)

# 미리 계산한 dp 배열을 사용하여 출력
for i in range(T):
    print(dp[n[i]])
