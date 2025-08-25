def solve(data):
    """
    - data: danh sach da doc tu input
    - data[0] = N
    - data[1] = K
    - tiep theo la N cap (key, val) tuan tu: key la string, val co the la so nguyen hoac string
    """
    N = data[0]
    K = data[1]
    idx = 2
    result = []
    for _ in range(N):
        key = data[idx]
        val = data[idx + 1]
        idx += 2
        # Kiem tra val co phai so nguyen hay khong
        try:
            val_int = int(val)
            if val_int > K:
                result.append(f"{key} {val}")
        except:
            # val khong phai so nguyen (chuoi)
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
