K = int(input())
num = [] * K
for i in range(K):
    n = int(input())
    num.append(n)
    
num.sort()
for j in range(K):
    print(num[j])