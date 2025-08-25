def solve(data):
    """
    data: danh sach gom [N, key1, value1, key2, value2, ..., keyN, valueN]
    """
    N = data[0]
    keys = []
    values = []
    idx = 1
    for _ in range(N):
        key = data[idx]
        value = data[idx + 1]
        keys.append(key)
        values.append(value)
        idx += 2
    
    result = []
    # Duyet tu cuoi ve dau
    for i in range(N - 1, -1, -1):
        pos = N - i  # vi tri dao nguoc, bat dau tu 1
        val_new = values[i] * pos
        result.append(f"{keys[i]} {val_new}")
    return result

def main():
    data = []
    N = int(input().strip())
    data.append(N)
    for _ in range(N):
        line = input().strip().split()
        key = line[0]
        value = int(line[1])
        data.extend([key, value])
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()
