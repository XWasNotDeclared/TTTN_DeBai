# File: sub.py
def solve(data):
    """
    Hàm giải bài toán chuyển đổi múi giờ.
    - data: danh sách chứa input đã được đọc
    - Trả về: list chứa các dòng kết quả
    """
    idx = 0
    n = data[idx]
    idx += 1
    
    # Đọc thời gian Hà Nội (HH:MM)
    hanoi_time = data[idx]
    idx += 1
    
    # Tách giờ và phút
    hh, mm = map(int, hanoi_time.split(':'))
    hanoi_minutes = hh * 60 + mm  # Chuyển sang phút để tính toán
    
    result = []
    
    for _ in range(n):
        city_name = data[idx]
        offset = data[idx + 1]
        idx += 2
        
        # Tính thời gian mới
        new_minutes = hanoi_minutes + offset * 60
        
        # Xử lý vòng 24 giờ
        new_minutes = new_minutes % (24 * 60)
        if new_minutes < 0:
            new_minutes += 24 * 60
            
        # Chuyển về giờ:phút
        new_hh = new_minutes // 60
        new_mm = new_minutes % 60
        
        # Format output
        time_str = f"{new_hh:02d}:{new_mm:02d}"
        result.append(f"{city_name} {time_str}")
    
    return result

def main():
    data = []
    
    # Đọc số lượng thành phố
    n = int(input().strip())
    data.append(n)
    
    # Đọc thời gian Hà Nội
    hanoi_time = input().strip()
    data.append(hanoi_time)
    
    # Đọc thông tin từng thành phố
    for _ in range(n):
        line = input().strip().split()
        city_name = line[0]
        offset = int(line[1])
        data.extend([city_name, offset])
    
    # Giải và in kết quả
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()