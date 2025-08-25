def solve(data):
    """
    Ham giai bai toan Mario Physics Simulation.
    - data: danh sach so nguyen hoac chuoi da duoc doc tu input.
    - Tra ve: list chua vi tri cuoi cung cua Mario (x, y) voi 2 chu so thap phan.
    """
    idx = 0
    g = float(data[idx])
    dt = float(data[idx + 1])
    N = int(data[idx + 2])
    idx += 3
    
    # Vi tri va van toc ban dau
    x = float(data[idx])
    y = float(data[idx + 1])
    vx = float(data[idx + 2])
    vy = float(data[idx + 3])
    idx += 4
    
    # Xu ly tung khung thoi gian
    for i in range(N):
        action = data[idx]
        idx += 1
        
        # Xu ly hanh dong
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
            if y == 0:  # Chi nhay khi dang tren mat dat
                vy = v
        # NONE khong can xu ly gi them
        
        # Cap nhat van toc do trong luc
        vy = vy - g * dt
        
        # Cap nhat vi tri
        x = x + vx * dt
        y = y + vy * dt
        
        # Xu ly va cham voi mat dat
        if y < 0:
            y = 0
            vy = 0
    
    # Tra ve vi tri cuoi cung voi 2 chu so thap phan
    return [f"{x:.2f} {y:.2f}"]

def main():
    data = []
    
    # Doc dong dau tien: g dt N
    line1 = input().strip().split()
    data.extend(line1)
    
    # Doc dong thu hai: x0 y0 vx0 vy0
    line2 = input().strip().split()
    data.extend(line2)
    
    # Doc cac hanh dong
    N = int(line1[2])
    for _ in range(N):
        action_line = input().strip().split()
        data.extend(action_line)
    
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()