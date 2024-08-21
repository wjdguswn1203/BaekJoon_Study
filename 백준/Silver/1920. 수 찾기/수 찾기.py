# 백준 1920
n_num_target = int(input())
n_num_list = set(list(map(int, input().split(" "))))

m_num_target = int(input())
m_num_list = list(map(int, input().split(" ")))

for i in range(m_num_target):
  if m_num_list[i] in n_num_list:
    print(1)
  else:
    print(0)