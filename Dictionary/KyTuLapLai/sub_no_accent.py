def solve(data):
    """
    Ham giai bai toan 'Ky tu lap lai'.
    - data: danh sach (da doc tu input) gom chuoi can xu ly.
    - Tra ve: list chua 1 dong ket qua (string).
    """
    s = data[0]
    freq = {}
    duplicates = []

    # Dem tan suat ky tu
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    # Lay ky tu lap theo thu tu xuat hien dau tien
    for c in s:
        if freq[c] > 1 and c not in duplicates:
            duplicates.append(c)

    if duplicates:
        return [" ".join(duplicates)]
    else:
        return ["None"]


def main():
    data = []
    s = input().rstrip("\n")  # chi 1 chuoi
    data.append(s)
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
