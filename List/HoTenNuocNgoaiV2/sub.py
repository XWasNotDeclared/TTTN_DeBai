def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách chứa số test case và các tên
    - Trả về: list chứa các tên đã được đổi thứ tự
    """
    t = data[0]  # số test case
    result = []
    
    for i in range(1, t + 1):
        name = data[i]  # lấy tên thứ i
        words = name.split()  # tách thành các từ
        
        # Lấy các phần của tên
        ho = words[0]  # họ (từ đầu tiên)
        ten_chinh = words[-1]  # tên chính (từ cuối cùng)
        ten_dem = words[1:-1]  # các tên đệm (từ thứ 2 đến thứ n-1)
        
        # Tạo tên mới: Tên_chính + Họ + các Tên_đệm
        new_name_parts = [ten_chinh, ho] + ten_dem
        new_name = " ".join(new_name_parts)
        
        result.append(new_name)
    
    return result

def main():
    data = []
    t = int(input().strip())  # số test case
    data.append(t)
    
    for _ in range(t):
        name = input().strip()  # đọc từng tên
        data.append(name)
    
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()