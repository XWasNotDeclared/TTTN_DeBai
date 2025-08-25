def solve(data):
    """
    - data: danh sach dau vao da doc (theo format file input).
    - Tra ve: list cac ket qua tuong ung (moi tong diem tren 1 dong).
    """
    N = data[0]
    idx = 1
    matrix = []
    for _ in range(N):
        length = data[idx]
        idx += 1
        row = data[idx:idx+length]
        idx += length
        matrix.append(row)

    M = data[idx]
    idx += 1
    scoring = {}
    for _ in range(M):
        word = data[idx]
        point = data[idx+1]
        idx += 2
        scoring[word] = point

    # Tinh diem tung hang
    res = []
    for row in matrix:
        total = 0
        for w in row:
            # Neu tu khong co trong dict, diem = 0
            total += scoring.get(w, 0)
        res.append(total)

    return res


def main():
    data = []
    N = int(input().strip())
    data.append(N)
    for _ in range(N):
        row = input().strip().split()
        data.append(len(row))
        data.extend(row)
    M = int(input().strip())
    data.append(M)
    for _ in range(M):
        w, p = input().strip().split()
        data.append(w)
        data.append(int(p))
    res = solve(data)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
