input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:
        if number == element:
            return True

    return False


result = is_number_exist(3, input)
print(result)

#시간복잡도:N array의 길이만큼 연산실행 -> 조건문에서 비교연산 ->총 시간복잡도는 Nx1
#입력값에 비례해서 얼마나 늘어날지 파악. 공간복잡도 보다는 시간 복잡도를 더 줄이기위해 고민 최악의 경우에 시간이 얼마나 소요될지(빅오표기법)에 대해고민