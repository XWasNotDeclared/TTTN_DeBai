def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách số nguyên hoặc chuỗi đã được đọc từ input.
    - TODO: Viết logic giải ở đây.
    - Trả về: list (hoặc iterable) chứa các dòng kết quả (string hoặc số).
    """
    # Ví dụ: bài tính tổng của từng test case
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        result.append(a + b)  # thay bằng logic của bạn
    return result


def main():
    data = []
    t = int(input().strip())  # số test case
    data.append(t)
    for _ in range(t):
        a, b = map(int, input().split())
        data.extend([a, b])
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()