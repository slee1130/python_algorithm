current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# 0은 청소하지 안흥ㄴ 장소 1은 청소하지 못하는 장소 2는 청소한 장소
# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색을 진행한다. ->이 문제는 방향이라는 개념 존재. 왼쪽방향으로 회전한다는 개념을 구해야
# 갈 수 있는 모든 칸을 전부 탐색해야함 -> BFS


# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 방향 전환
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4


# 후진
def get_d_index_when_go_back(d):
    return (d + 2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_departments_cleaned = 1  # 청소하는 칸의 개수
    room_map[r][c] = 2
    queue = list([[r, c, d]])

    # 큐가 비어지면 종료
    while queue:
        r, c, d = queue.pop(0)
        temp_d = d

        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            # a
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break

            # c
            elif i == 3:  # 갈 곳이 없었던 경우
                new_r, new_c = r + dr[get_d_index_when_go_back(d)], c + dc[get_d_index_when_go_back(d)]
                queue.append([new_r, new_c, d])

                # d
                if room_map[new_r][new_c] == 1:  # 뒤가 벽인 경우
                    return count_of_departments_cleaned


print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))