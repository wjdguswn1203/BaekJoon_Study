# [Bronze II] 피보나치 수 5 - 10870 

[문제 링크](https://www.acmicpc.net/problem/10870) 

## 📌 문제 번호

- 문제 번호: 10870

## 📚 사용한 자료구조/알고리즘

- 자료구조/알고리즘: 재귀함수

## 🔍 문제의 핵심 포인트

- 문제를 이해하는 데 중요한 부분:
- 피보나치 수열에 대해 이해하고 이를 재귀함수를 통해 적용

## ⏱️ 코드의 시간복잡도

- 시간복잡도:
- 재귀함수에서 fibo(m-1) + fibo(m-2) 이 부분으로 호출 트리를 생성하여 이진 트리로 확장됨.
- 그렇기에 호출의 수가 두배로 증가
- T(n)=T(n−1)+T(n−2)+O(1) => O(n^2)
- 시간복잡도는 `O(n^2)`이다.

## 🧠 코드의 공간복잡도

- 공간복잡도:
- 함수의 호출 스택만 소비하기 때문에 최대 깊이는 `n`
- 공간복잡도는 `O(n)`이다.


### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

구현, 수학

### 제출 일자

2024년 8월 28일 22:02:40

### 문제 설명

<p>피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.</p>

<p>이를 식으로 써보면 F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub> (n ≥ 2)가 된다.</p>

<p>n=17일때 까지 피보나치 수를 써보면 다음과 같다.</p>

<p>0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597</p>

<p>n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.</p>

### 출력 

 <p>첫째 줄에 n번째 피보나치 수를 출력한다.</p>

