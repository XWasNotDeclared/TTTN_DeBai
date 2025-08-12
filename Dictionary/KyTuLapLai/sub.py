def solve(data):
    """
    Hàm giải bài toán 'Ký tự lặp lại'.
    - data: danh sách (đã đọc từ input) gồm chuỗi cần xử lý.
    - Trả về: list chứa 1 dòng kết quả (string).
    """
    s = data[0]
    freq = {}
    duplicates = []

    # Đếm tần suất ký tự
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    # Lấy ký tự lặp theo thứ tự xuất hiện đầu tiên
    for c in s:
        if freq[c] > 1 and c not in duplicates:
            duplicates.append(c)

    if duplicates:
        return [" ".join(duplicates)]
    else:
        return ["None"]


def main():
    data = []
    s = input().rstrip("\n")  # chỉ 1 chuỗi
    data.append(s)
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
