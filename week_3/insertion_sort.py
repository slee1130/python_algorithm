input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break


insertion_sort(input)
print(input)

# 이것도 바로 O(N^2) 만큼 걸립니다.
#
# 그러나, 버블 정렬과 선택 정렬과 다른 면이 있습니다.
# 버블 정렬과 선택 정렬은 최선이든 최악이든 항~~상 O(N^2) 만큼의 시간이 걸렸지만,
#
# 최선의 경우에는 Ω(N) 만큼의 시간 복잡도가 걸립니다.
# 거의 정렬이 된 배열이 들어간다면 break 문에 의해서
# 더 많은 원소와 비교하지 않고 탈출할 수 있기 때문입니다!