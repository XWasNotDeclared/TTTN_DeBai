def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach so nguyen hoac chuoi da duoc doc tu input.
    - Tra ve: list chua cac dong ket qua (string hoac so).
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        a = int(data[idx])
        b = float(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        
        # 1. Tong a + b (2 chu so thap phan)
        result.append(f"{a + b:.2f}")
        
        # 2. Binh phuong cua a
        result.append(str(a * a))
        
        # 3. Lap chuoi hoac EMPTY
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
        data.extend(parts)  # giu nguyen dang chuoi de xu ly sau
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
