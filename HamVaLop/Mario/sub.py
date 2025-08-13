def solve(data):
    """
    Hàm giải bài toán Mario Physics Simulation.
    - data: danh sách số nguyên hoặc chuỗi đã được đọc từ input.
    - Trả về: list chứa vị trí cuối cùng của Mario (x, y) với 2 chữ số thập phân.
    """
    idx = 0
    g = float(data[idx])
    dt = float(data[idx + 1])
    N = int(data[idx + 2])
    idx += 3
    
    # Vị trí và vận tốc ban đầu
    x = float(data[idx])
    y = float(data[idx + 1])
    vx = float(data[idx + 2])
    vy = float(data[idx + 3])
    idx += 4
    
    # Xử lý từng khung thời gian
    for i in range(N):
        action = data[idx]
        idx += 1
        
        # Xử lý hành động
        if action == "LEFT":
            a = float(data[idx])
            idx += 1
            vx = vx - a * dt
        elif action == "RIGHT":
            a = float(data[idx])
            idx += 1
            vx = vx + a * dt
        elif action == "JUMP":
            v = float(data[idx])
            idx += 1
            if y == 0:  # Chỉ nhảy khi đang trên mặt đất
                vy = v
        # NONE không cần xử lý gì thêm
        
        # Cập nhật vận tốc do trọng lực
        vy = vy - g * dt
        
        # Cập nhật vị trí
        x = x + vx * dt
        y = y + vy * dt
        
        # Xử lý va chạm với mặt đất
        if y < 0:
            y = 0
            vy = 0
    
    # Trả về vị trí cuối cùng với 2 chữ số thập phân
    return [f"{x:.2f} {y:.2f}"]

def main():
    data = []
    
    # Đọc dòng đầu tiên: g dt N
    line1 = input().strip().split()
    data.extend(line1)
    
    # Đọc dòng thứ hai: x0 y0 vx0 vy0
    line2 = input().strip().split()
    data.extend(line2)
    
    # Đọc các hành động
    N = int(line1[2])
    for _ in range(N):
        action_line = input().strip().split()
        data.extend(action_line)
    
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()