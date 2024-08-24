# 백준 10773
K = int(input())
input_list = [] * K
sum = 0

for i in range(K):
  num = int(input())
  if num == 0:
    sum -= input_list[-1]
    input_list.pop()
  else:
    sum += num
    input_list.append(num)

print(sum)
