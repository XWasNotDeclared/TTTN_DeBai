def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach chuoi da duoc doc tu input.
    - Tra ve: list chua cac dong ket qua (string).
    """
    t = int(data[0])
    idx = 1
    result = []
    for _ in range(t):
        s = data[idx]
        idx += 1

        if s.isdigit():
            result.append("INT")
        elif s.replace('.', '', 1).isdigit() and '.' in s:
            result.append("FLOAT")
        elif s == "True" or s == "False":
            result.append("BOOL")
        else:
            result.append("STRING")

    return result


def main():
    data = []
    t = int(input().strip())  # so test case
    data.append(str(t))
    for _ in range(t):
        s = input().strip()
        data.append(s)
    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()
