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
    t = int(input().strip())  # so test case
    data.append(t)
    for _ in range(t):
        a, b, c = map(int, input().split())
        data.extend([a, b, c])
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()