shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# 첫번째 solution

def is_available_to_order(menus, orders):
    menus.sort()  # menus 정렬!
    for order in orders:
        if not is_existing_target_number_binary(order, menus):
            return False
    return True


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)

#위의 솔루션:우선, menus 를 정렬합니다.
# menus 의 길이를 N 이라고 한다면 O(N * log N) 의 연산이 필요합.
# 그리고 정렬된 menus 내에서 이진 탐색의 시간 복잡도는 O(log N).
# 이걸 orders의 개수 M 만큼 반복하게 되므로 O(M * logN) 의 연산이 필요.
# 즉, O((M+N)*logn) 만큼의 시간 복잡도가 소요

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)

# 집합자료형을 사용한 두번째 솔루션 -> 단순 특정한 문자열이 배열에 존재하는지만 확인하면 되는 문제
# 집합은 중복을 허용하지않는 자료형
# menus 를 menus_set 으로 만들기 위해서는
# orders 의 길이를 N 이라고 한다면 O(N) 의 연산이 필요
#
# 그리고 집합 내에서 탐색의 시간 복잡도는 O(1)
# 이걸 주문의 개수 M 만큼 반복하게 되므로 O(M) 의 연산이 필요
#
# 즉, O(M+N) 만큼의 시간 복잡도가 소요 -> 첫번쨰 솔루션보다 훨씬 효율적인 방법
