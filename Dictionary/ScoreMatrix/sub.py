def solve(data):
    """
    - data: danh sách đầu vào đã đọc (theo format file input).
    - Trả về: list các kết quả tương ứng (mỗi tổng điểm trên 1 dòng).
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

    # Tính điểm từng hàng
    res = []
    for row in matrix:
        total = 0
        for w in row:
            # Nếu từ không có trong dict, điểm = 0
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
