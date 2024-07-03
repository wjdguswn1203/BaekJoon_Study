# 스택
def push(n):
  stack.append(n)
def pop():
  if len(stack) == 0:
    print("-1")
  else:
    print(stack[-1])
    stack.pop()
def size():
  print(len(stack))
def empty():
  if len(stack) == 0:
    print("1")
  else:
    print("0")
def top():
  if len(stack) == 0:
    print("-1")
  else:
    print(stack[-1])

stack = []
n_list = []
command_num = int(input())
for cmd in range(command_num):
  n_list.append(input())
  
for i in range(len(n_list)):
  cmd_list = n_list[i].split(" ")
  if cmd_list[0] == "push":
    push(int(cmd_list[1]))
  if cmd_list[0] == "pop":
    pop()
  if cmd_list[0] == "size":
    size()
  if cmd_list[0] == "empty":
    empty()
  if cmd_list[0] == "top":
    top()
  