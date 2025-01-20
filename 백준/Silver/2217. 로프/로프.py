n = int(input())
ropes = [int(input()) for _ in range(n)]  # 로프의 중량 한계 입력

ropes.sort(reverse=True)  # 내림차순 정렬

# 각 로프를 사용할 때의 최대 중량 계산
max_weight = 0
for i in range(n):
    max_weight = max(max_weight, ropes[i] * (i + 1))

print(max_weight)
