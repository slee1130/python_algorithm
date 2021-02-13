input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


bubble_sort(input)
print(input)

# 버블 정렬 시간 복잡도: o(n^2) 2차 반복문이 나오고 array 길이 만큼 반복하는 경우 -> o(n^2)