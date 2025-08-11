def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách số nguyên hoặc chuỗi đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string hoặc số).
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        a = int(data[idx])
        b = float(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        
        # 1. Tổng a + b (2 chữ số thập phân)
        result.append(f"{a + b:.2f}")
        
        # 2. Bình phương của a
        result.append(str(a * a))
        
        # 3. Lặp chuỗi hoặc EMPTY
        if a > 0:
            result.append(s * a)
        else:
            result.append("EMPTY")
    return result


def main():
    data = []
    t = int(input().strip())
    data.append(t)
    for _ in range(t):
        # a: int, b: float, s: string
        parts = input().split()
        data.extend(parts)  # giữ nguyên dạng chuỗi để xử lý sau
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
