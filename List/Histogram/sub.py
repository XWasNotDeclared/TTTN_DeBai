def solve(data):
    """
    Hàm giải bài toán tính histogram ảnh xám.
    - data: danh sách số nguyên đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
    """
    idx = 0
    H, W = data[idx], data[idx + 1]
    idx += 2
    
    # Đọc ma trận ảnh và tính histogram đồng thời
    histogram = [0] * 256  # Mảng đếm cho 256 mức xám (0-255)
    
    for i in range(H):
        for j in range(W):
            pixel_value = data[idx]
            histogram[pixel_value] += 1
            idx += 1
    
    # Tạo kết quả chỉ với các mức xám xuất hiện ít nhất một lần
    result = []
    for gray_level in range(256):
        if histogram[gray_level] > 0:
            result.append(f"{gray_level} {histogram[gray_level]}")
    
    return result

def main():
    data = []
    H, W = map(int, input().split())
    data.extend([H, W])
    
    for _ in range(H):
        row = list(map(int, input().split()))
        data.extend(row)
    
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()