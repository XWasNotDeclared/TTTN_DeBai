def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách dữ liệu đã được đọc từ input (kiểu string).
    - Trả về: list chứa các dòng kết quả (string).
    """
    t = int(data[0])  # số test case
    idx = 1
    result = []
    for _ in range(t):
        s = data[idx]  # lấy chuỗi
        idx += 1
        num_chars = len(s)
        num_words = len(s.strip().split()) if s.strip() else 0
        num_upper = sum(1 for c in s if c.isupper())
        result.append(f"{num_chars} {num_words} {num_upper}")
    return result

def main():
    data = []
    t = int(input().strip())  # số test case
    data.append(str(t))
    for _ in range(t):
        s = input()  # đọc cả dòng, kể cả khoảng trắng
        data.append(s)
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()
