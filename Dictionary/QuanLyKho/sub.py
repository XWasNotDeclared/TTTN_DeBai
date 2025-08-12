def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách (đã đọc từ input) gồm cả số và chuỗi.
    - Trả về: list chứa các kết quả của từng truy vấn.
    """
    idx = 0
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1

    inventory = {}  # dictionary lưu tên -> giá trị tồn kho

    # Nhập hàng
    for _ in range(n):
        name = data[idx]; idx += 1
        value = int(data[idx]); idx += 1
        inventory[name] = inventory.get(name, 0) + value

    results = []

    # Xử lý truy vấn
    for _ in range(q):
        k = int(data[idx]); idx += 1
        total = 0
        for __ in range(k):
            name = data[idx]; idx += 1
            total += inventory.get(name, 0)
        results.append(total)

    return results


def main():
    data = []
    n, q = map(int, input().split())
    data.extend([n, q])

    for _ in range(n):
        name, value = input().split()
        data.append(name)
        data.append(int(value))

    for _ in range(q):
        parts = input().split()
        k = int(parts[0])
        data.append(k)
        data.extend(parts[1:])

    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
