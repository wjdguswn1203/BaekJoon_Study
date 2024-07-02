# 백준 17103: 골드바흐 파티션
import math
# 배열의 크기를 받아옴
ary_num = int(input())
ary = []

# 배열의 크기만큼 입력을 받아옴
for i in range(ary_num):
  ary.append(int(input()))

# int(math.sqrt(max(ary)+1))
# 소수를 구하기
prime_ary = []
n = max(ary)
chk = [True]*(n+1)
res = []
chk[0], chk[1] = False, False
for i in range(2,int(math.sqrt(n)+1)):
  if chk[i]:
    res.append(i)
    j = 2
    while i*j <= n:
      chk[i*j] = False
      j += 1
prime_ary = [x for x in range(n+1) if chk[x]]
  
# 소수끼리 더하다가, 리스트의 원소와 동일해지면 중지하고 count를 출력
for num in ary:
  count = 0
  for i in prime_ary:
      if i > num // 2:
          break
      if chk[num - i]:
          count += 1
  print(count)
