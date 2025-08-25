def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach du lieu da doc tu input.
    - Moi test case gom:
        name (str)
        price (float)
        quantity (int)
        promo (str)
    - Tra ve: list chua cac dong ket qua (string).
    """
    t = int(data[0])
    idx = 1
    result = []
    for _ in range(t):
        name = data[idx]
        price = float(data[idx + 1])
        quantity = int(data[idx + 2])
        promo = data[idx + 3].lower()
        idx += 4

        total_value = price * quantity
        if promo == "yes":
            total_value *= 0.9

        result.append(f"Product: {name}")
        result.append(f"Total value: {total_value:.2f} USD")

    return result


def main():
    data = []
    t = int(input().strip())  # so test case
    data.append(t)
    for _ in range(t):
        name = input().strip()
        price = input().strip()
        quantity = input().strip()
        promo = input().strip()
        data.extend([name, price, quantity, promo])
    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()
