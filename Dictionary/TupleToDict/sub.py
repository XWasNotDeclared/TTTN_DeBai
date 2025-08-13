def solve(data):
    """
    data: danh sách đọc từ input, cấu trúc: [N, key1, val1, key2, val2, ..., keyN, valN]
    key là chuỗi, value là số nguyên.
    Trả về: list gồm 1 chuỗi duy nhất là dict dưới dạng string.
    """
    n = data[0]
    keys = data[1:1+2*n:2]
    vals = data[2:1+2*n:2]
    d = {}
    for i in range(n):
        d[keys[i]] = vals[i]
    return [str(d)]

def main():
    data = []
    n = int(input().strip())
    data.append(n)
    for _ in range(n):
        k, v = input().split()
        data.append(k)
        data.append(int(v))
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()
