def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach du lieu da duoc doc tu input (kieu string).
    - Tra ve: list chua cac dong ket qua (string).
    """
    t = int(data[0])  # so test case
    idx = 1
    result = []
    for _ in range(t):
        s = data[idx]  # lay chuoi
        idx += 1
        num_chars = len(s)
        num_words = len(s.strip().split()) if s.strip() else 0
        num_upper = sum(1 for c in s if c.isupper())
        result.append(f"{num_chars} {num_words} {num_upper}")
    return result

def main():
    data = []
    t = int(input().strip())  # so test case
    data.append(str(t))
    for _ in range(t):
        s = input()  # doc ca dong, ke ca khoang trang
        data.append(s)
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()
