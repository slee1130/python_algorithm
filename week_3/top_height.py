top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:
        height = heights.pop()
        for idx in range(len(heights) - 1, -1, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

# 시간 복잡도: o(n^2) heights의 길이만큼 while문을 쓰는데 내부에 for 문이 len(heights)만큼 도니까 o(n^2)

