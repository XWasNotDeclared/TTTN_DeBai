def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach so nguyen hoac chuoi da duoc doc tu input.
    - TODO: Viet logic giai o day.
    - Tra ve: list (hoac iterable) chua cac dong ket qua (string hoac so).
    """
    # Vi du: bai tinh tong cua tung test case
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        result.append(a + b)  # thay bang logic cua ban
    return result


def main():
    data = []
    t = int(input().strip())  # so test case
    data.append(t)
    for _ in range(t):
        a, b = map(int, input().split())
        data.extend([a, b])
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()