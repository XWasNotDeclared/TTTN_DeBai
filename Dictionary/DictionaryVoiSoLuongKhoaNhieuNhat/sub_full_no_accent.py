def solve(data):
    """
    - data: danh sach chuoi, moi phan tu la mot dong dictionary duoi dang "key:value,key:value,..."
    - Tra ve so luong khoa nhieu nhat trong danh sach.
    """
    N = data[0]
    max_keys = 0
    for i in range(1, N + 1):
        line = data[i]
        if line == "":
            count_keys = 0
        else:
            pairs = line.split(',')
            count_keys = len(pairs)
        if count_keys > max_keys:
            max_keys = count_keys
    return [max_keys]


def main():
    data = []
    N = int(input().strip())
    data.append(N)
    for _ in range(N):
        line = input().strip()
        data.append(line)
    res = solve(data)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
