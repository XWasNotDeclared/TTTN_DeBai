def solve(data):
    """
    Ham giai bai toan tinh histogram anh xam.
    - data: danh sach so nguyen da duoc doc tu input.
    - Tra ve: list chua cac dong ket qua (string).
    """
    idx = 0
    H, W = data[idx], data[idx + 1]
    idx += 2
    
    # Doc ma tran anh va tinh histogram dong thoi
    histogram = [0] * 256  # Mang dem cho 256 muc xam (0-255)
    
    for i in range(H):
        for j in range(W):
            pixel_value = data[idx]
            histogram[pixel_value] += 1
            idx += 1
    
    # Tao ket qua chi voi cac muc xam xuat hien it nhat mot lan
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