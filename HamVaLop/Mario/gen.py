import os

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

def prepare_working_dir():
    """
    Chuyển thư mục làm việc về nơi chứa script hiện tại.
    Tìm và trả về danh sách tất cả các file .in trong thư mục đó.
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    """
    Xử lý một file .in và tạo file .out tương ứng.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu từ file input
        lines = fin.read().strip().split('\n')
        data = []
        
        # Đọc g dt N
        line1 = lines[0].split()
        data.extend(line1)
        
        # Đọc x0 y0 vx0 vy0
        line2 = lines[1].split()
        data.extend(line2)
        
        # Đọc các hành động
        N = int(line1[2])
        for i in range(2, 2 + N):
            action_line = lines[i].split()
            data.extend(action_line)
        
        # Gọi hàm giải
        res = solve(data)
        
        # Ghi kết quả ra file output
        fout.write("\n".join(map(str, res)) + "\n")

def main():
    """
    Hàm chính: tìm các file input, xử lý từng file, tạo file output.
    """
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()