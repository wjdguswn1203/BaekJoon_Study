def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        m = A[i] * B[len(B) - i - 1]
        answer += m

    return answer