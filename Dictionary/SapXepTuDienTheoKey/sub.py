def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách số nguyên hoặc chuỗi đã được đọc từ input.
    - TODO: Viết logic giải ở đây.
    - Trả về: list (hoặc iterable) chứa các dòng kết quả (string hoặc số).
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        pairs = []
        for __ in range(n):
            key = data[idx]
            value = data[idx + 1]
            idx += 2
            pairs.append((key, value))
        # Sắp xếp theo key (chuỗi)
        pairs.sort(key=lambda x: x[0])
        for key, val in pairs:
            result.append(f"{key} {val}")
    return result


def main():
    data = []
    t = int(input().strip())  # số test case
    data.append(t)
    for _ in range(t):
        n = int(input().strip())
        data.append(n)
        for __ in range(n):
            line = input().strip().split()
            key = line[0]
            value = int(line[1])
            data.extend([key, value])
    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()
