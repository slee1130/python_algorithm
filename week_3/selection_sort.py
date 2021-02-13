input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]


selection_sort(input)
print(input)

# 버블정렬하고 다른 부분: 최소값을 찾아서 변경하는것 -> min_index라는 변수를 통해 각각의 인덱스들과 비교
# 그리고 내부의 반복문이 끝나면 최소값의 인덱스와 i의 값들을 교체하면됨
# 이 함수의 시간복잡도 ->버블정렬과 같은 o(n^2) 2차반복문 나오고 array의 길이만큼 반복