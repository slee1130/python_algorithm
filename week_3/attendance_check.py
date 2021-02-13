all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    dict = {}
    for key in all_array:
        dict[key] = True  # 아무 값이나 넣어도 상관 없습니다! 여기서는 키가 중요한거니까요

    for key in present_array:  # dict에서 key 를 하나씩 없앱니다
        del dict[key]

    for key in dict.keys():  # key 중에 하나를 바로 반환합니다! 한 명 밖에 없으니 이렇게 해도 괜찮습니다.
        return key


print(get_absent_student(all_students, present_students))

# 이 함수의 시간 복잡도는 o(n)만큼 걸림 all_array의 길이를 n 이라고 하면, 반복문은 몇개 안됨 대신, 공간복잡도도 o(n)만큼 걸림
# 모든 학생들을 다 해쉬테이블 내에 저장 해야하기때문 . 해쉬테이블은 시간은 빠르지만 공간을 대신 사용하는 자료구조