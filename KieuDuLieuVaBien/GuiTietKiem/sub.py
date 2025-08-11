def solve(data):
    """
    Hàm giải bài toán Sổ tiết kiệm.
    - data: danh sách dữ liệu đã đọc từ input.
    - Trả về: list chứa các kết quả (int) của từng test case.
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        A = data[idx]
        r = data[idx + 1]
        n = data[idx + 2]
        idx += 3
        # Tính lãi kép
        final_amount = A * ((1 + r / 100) ** n)
        result.append(int(final_amount))  # làm tròn xuống
    return result


def main():
    data = []
    t = int(input().strip())  # số test case
    data.append(t)
    for _ in range(t):
        A, r, n = input().split()
        data.append(int(A))
        data.append(float(r))
        data.append(int(n))
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
