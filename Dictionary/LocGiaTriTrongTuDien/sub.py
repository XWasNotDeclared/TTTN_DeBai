def solve(data):
    """
    - data: danh sách đã đọc từ input
    - data[0] = N
    - data[1] = K
    - tiếp theo là N cặp (key, val) tuần tự: key là string, val có thể là số nguyên hoặc string
    """
    N = data[0]
    K = data[1]
    idx = 2
    result = []
    for _ in range(N):
        key = data[idx]
        val = data[idx + 1]
        idx += 2
        # Kiểm tra val có phải số nguyên hay không
        try:
            val_int = int(val)
            if val_int > K:
                result.append(f"{key} {val}")
        except:
            # val không phải số nguyên (chuỗi)
            result.append(f"{key} {val}")

    if not result:
        result.append("Empty")
    return result

def main():
    data = []
    N = int(input().strip())
    K = int(input().strip())
    data.append(N)
    data.append(K)
    for _ in range(N):
        parts = input().strip().split()
        key = parts[0]
        val = parts[1]
        data.extend([key, val])
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()
