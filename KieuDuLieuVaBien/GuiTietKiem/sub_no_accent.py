def solve(data):
    """
    Ham giai bai toan So tiet kiem.
    - data: danh sach du lieu da doc tu input.
    - Tra ve: list chua cac ket qua (int) cua tung test case.
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        A = data[idx]
        r = data[idx + 1]
        n = data[idx + 2]
        idx += 3
        # Tinh lai kep
        final_amount = A * ((1 + r / 100) ** n)
        result.append(int(final_amount))  # lam tron xuong
    return result


def main():
    data = []
    t = int(input().strip())  # so test case
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
