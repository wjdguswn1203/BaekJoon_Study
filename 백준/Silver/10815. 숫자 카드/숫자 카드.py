# 백준 10815
card_num = int(input())
card_list = set(list(map(int, input().split(" "))))

m_num = int(input())
m_list = list(map(int, input().split(" ")))

for i in range(m_num):
  if m_list[i] in card_list:
    print(1)
  else:
    print(0)

   
