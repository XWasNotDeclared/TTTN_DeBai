def solve(data):
    """
    - data: danh sách các dòng đã đọc từ input, theo format:
      [N, key1_1, val1_1, key1_2, val1_2, ..., M, key2_1, val2_1, ...]
    - Trả về: list các chuỗi kết quả theo yêu cầu đề bài.
    """
    idx = 0
    N = data[idx]
    idx += 1

    dict1 = {}
    order1 = []  # lưu thứ tự khóa xuất hiện ở dict1
    for _ in range(N):
        key = data[idx]
        val = data[idx + 1]
        idx += 2
        dict1[key] = val
        order1.append(key)

    M = data[idx]
    idx += 1

    dict2 = {}
    order2 = []  # lưu thứ tự khóa xuất hiện ở dict2
    for _ in range(M):
        key = data[idx]
        val = data[idx + 1]
        idx += 2
        dict2[key] = val
        order2.append(key)

    # Gộp dict1 và dict2: khóa dict2 ghi đè dict1
    result_dict = dict1.copy()
    for k, v in dict2.items():
        result_dict[k] = v

    # In theo thứ tự đề bài:
    # các khóa dict1 theo thứ tự xuất hiện (đã lưu), đã cập nhật nếu có dict2 ghi đè
    # rồi đến các khóa dict2 mà không có trong dict1
    output = []
    used = set()

    for k in order1:
        output.append(f"{k} {result_dict[k]}")
        used.add(k)

    for k in order2:
        if k not in used:
            output.append(f"{k} {result_dict[k]}")

    return output


def main():
    data = []
    N = int(input().strip())
    data.append(N)
    for _ in range(N):
        key, val = input().split()
        data.append(key)
        data.append(int(val))

    M = int(input().strip())
    data.append(M)
    for _ in range(M):
        key, val = input().split()
        data.append(key)
        data.append(int(val))

    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()
