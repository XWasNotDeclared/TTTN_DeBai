def solve(data):
    """
    - data: danh sách chuỗi, mỗi phần tử là một dòng dictionary dưới dạng "key:value,key:value,..."
    - Trả về số lượng khóa nhiều nhất trong danh sách.
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
