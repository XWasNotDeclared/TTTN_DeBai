def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach so nguyen hoac chuoi da duoc doc tu input.
    - TODO: Viet logic giai o day.
    - Tra ve: list (hoac iterable) chua cac dong ket qua (string hoac so).
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        pairs = []
        for __ in range(n):
            key = data[idx]
            value = data[idx + 1]
            idx += 2
            pairs.append((key, value))
        # Sap xep theo key (chuoi)
        pairs.sort(key=lambda x: x[0])
        for key, val in pairs:
            result.append(f"{key} {val}")
    return result


def main():
    data = []
    t = int(input().strip())  # so test case
    data.append(t)
    for _ in range(t):
        n = int(input().strip())
        data.append(n)
        for __ in range(n):
            line = input().strip().split()
            key = line[0]
            value = int(line[1])
            data.extend([key, value])
    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()
