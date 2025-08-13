def solve(data):
    """
    data = [N, K, key1, val1, key2, val2, ..., keyN, valN]
    """
    N = data[0]
    K = data[1]
    res = []
    idx = 2
    while idx < 2 + 2 * N:
        sub_dict = []
        for _ in range(K):
            if idx >= 2 + 2 * N:
                break
            key = data[idx]
            val = data[idx + 1]
            sub_dict.append(f"{key}:{val}")
            idx += 2
        res.append(" ".join(sub_dict))
    return res

def main():
    import sys
    input = sys.stdin.readline
    # Đọc N, K
    N, K = map(int, input().strip().split())
    data = [N, K]
    for _ in range(N):
        line = input().strip().split()
        key = line[0]
        val = int(line[1])
        data.append(key)
        data.append(val)
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()
