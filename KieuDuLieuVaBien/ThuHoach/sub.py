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
        t = data[idx]
        k = data[idx + 1]
        n = data[idx + 2]
        idx += 3
       #print(t, k, n)
        if t<=n and not k == 0:
            result.append((n-t)//k+1)   
        else:
            result.append(0)
    return result


def main():
    data = []
    t = int(input().strip())  # số test case
    data.append(t)
    for _ in range(t):
        a, b, c = map(int, input().split())
        data.extend([a, b, c])
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()