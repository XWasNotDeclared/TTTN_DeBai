def solve(data):
    """
    Hàm giải bài toán cân bằng histogram.
    - data: danh sách số nguyên đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
    """
    idx = 0
    N, M = data[idx], data[idx + 1]
    idx += 2
    
    # Đọc ma trận ảnh
    image = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(data[idx])
            idx += 1
        image.append(row)
    
    # Bước 1: Tính histogram gốc
    histogram = [0] * 256
    for i in range(N):
        for j in range(M):
            histogram[image[i][j]] += 1
    
    # Bước 2: Tính CDF (Cumulative Distribution Function)
    cdf = [0] * 256
    cdf[0] = histogram[0]
    for k in range(1, 256):
        cdf[k] = cdf[k-1] + histogram[k]
    
    # Bước 3: Cân bằng histogram
    total_pixels = N * M
    result_image = []
    
    for i in range(N):
        row_result = []
        for j in range(M):
            old_value = image[i][j]
            # Tính giá trị mới: new_value = round(255 * cdf[old_value] / total_pixels)
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