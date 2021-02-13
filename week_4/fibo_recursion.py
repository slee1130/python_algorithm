input = 20


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))

# recursion을 썻을경우 -> 실행하는 연산시간이 너무 오래 걸려 값이 나오질않음  -> 이럴때 쓰는게 동적계획법 (dynamic programming)
# dynamic programming이란 : 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법. 이것은 부분 문제 반복과 최적 부분 구조를 가지고있는
# 알고리즘을 일반적인 방법에 비해 더욱 적은 시간내에 풀때 사용됨
# 여러개의 하위 문제를 풀고 그 결과를 기록하고 이용해 문제를 해결하는 알고리즘
# 문제를 쪼개서 정의 할 수 있으면 동적 계획법 가능 -> 이처럼 문제를 반복해서 해결해 나가는 모습이 재귀 함수와 닮은
# 그러나 다른점은 그 결과를 기록하고 이용한다는 것 -> 결과를 기롯하는것을 memoization이라고 하고 문제를 쪼갤수 있는 구조를 겹치는 부분문제
# overlapping subproblem이라고 함. 즉 겹치는 부분 문제일 경우 동적 계획법을 사용하면됨. 이때 사용하는 방법은 메모이제이션이용