import os

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
    
    with open(infile, "r", encoding='utf-8') as fin:
        lines = [line.strip() for line in fin.readlines() if line.strip()]
    
    # Parse input theo format của bài
    data = []
    idx = 0
    
    # Số lượng thành phố
    n = int(lines[idx])
    data.append(n)
    idx += 1
    
    # Thời gian Hà Nội
    hanoi_time = lines[idx]
    data.append(hanoi_time)
    idx += 1
    
    # Thông tin từng thành phố
    for _ in range(n):
        parts = lines[idx].split()
        city_name = parts[0]
        offset = int(parts[1])
        data.extend([city_name, offset])
        idx += 1
    
    # Gọi hàm giải
    res = solve(data)
    
    # Ghi kết quả ra file output
    with open(outfile, "w", encoding='utf-8') as fout:
        fout.write("\n".join(res) + "\n")

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