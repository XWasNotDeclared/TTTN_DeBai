def solve(data):
    """
    Ham giai bai toan can bang histogram.
    - data: danh sach so nguyen da duoc doc tu input.
    - Tra ve: list chua cac dong ket qua (string).
    """
    idx = 0
    N, M = data[idx], data[idx + 1]
    idx += 2
    
    # Doc ma tran anh
    image = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(data[idx])
            idx += 1
        image.append(row)
    
    # Buoc 1: Tinh histogram goc
    histogram = [0] * 256
    for i in range(N):
        for j in range(M):
            histogram[image[i][j]] += 1
    
    # Buoc 2: Tinh CDF (Cumulative Distribution Function)
    cdf = [0] * 256
    cdf[0] = histogram[0]
    for k in range(1, 256):
        cdf[k] = cdf[k-1] + histogram[k]
    
    # Buoc 3: Can bang histogram
    total_pixels = N * M
    result_image = []
    
    for i in range(N):
        row_result = []
        for j in range(M):
            old_value = image[i][j]
            # Tinh gia tri moi: new_value = round(255 * cdf[old_value] / total_pixels)
            new_value = round(255 * cdf[old_value] / total_pixels)
            row_result.append(str(new_value))
        result_image.append(' '.join(row_result))
    
    return result_image

def main():
    data = []
    N, M = map(int, input().split())
    data.extend([N, M])
    
    for _ in range(N):
        row = list(map(int, input().split()))
        data.extend(row)
    
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()