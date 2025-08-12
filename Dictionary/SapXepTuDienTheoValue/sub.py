def solve(data):
    """
    - data: danh sách dữ liệu đầu vào đã đọc.
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        pairs = []
        for __ in range(n):
            key, value = data[idx]
            idx += 1
            pairs.append((key, value))
        # Sắp xếp theo value tăng dần, nếu bằng thì theo key tăng dần
        pairs.sort(key=lambda x: (x[1], x[0]))
        for p in pairs:
            result.append(f"{p[0]} {p[1]}")
    return result


def main():
    data = []
    t = int(input().strip())
    data.append(t)
    for _ in range(t):
        n = int(input().strip())
        data.append(n)
        for __ in range(n):
            line = input().strip().split()
            key = line[0]
            value = int(line[1])
            data.append((key, value))
    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()