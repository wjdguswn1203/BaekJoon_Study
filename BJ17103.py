# 백준 17103: 골드바흐 파티션

# 배열의 크기를 받아옴
ary_num = int(input())
ary = []

# 배열의 크기만큼 입력을 받아옴
for i in range(ary_num):
  ary.append(int(input()))

# int(math.sqrt(max(ary)+1))
# 소수를 구하기
prime_ary = []
for i in range(2,max(ary)+1):
  for j in range(2, i+1):
    if j==i:
      prime_ary.append(j)
    if i%j == 0:
      break
  
# 소수끼리 더하다가, 리스트의 원소와 동일해지면 중지하고 count를 출력
for num in ary:
  count = 0
  for i in prime_ary:
    for j in prime_ary:
      if(num == i+j):
        count += 1
  if count > 1:
    count = round(count/2)
  print(count)
