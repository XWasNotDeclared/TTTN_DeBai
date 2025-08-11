def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách chuỗi đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
    """
    t = int(data[0])
    idx = 1
    result = []
    for _ in range(t):
        s = data[idx]
        idx += 1

        if s.isdigit():
            result.append("INT")
        elif s.replace('.', '', 1).isdigit() and '.' in s:
            result.append("FLOAT")
        elif s == "True" or s == "False":
            result.append("BOOL")
        else:
            result.append("STRING")

    return result


def main():
    data = []
    t = int(input().strip())  # số test case
    data.append(str(t))
    for _ in range(t):
        s = input().strip()
        data.append(s)
    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()
