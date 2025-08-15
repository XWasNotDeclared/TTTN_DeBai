import os

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
    
    with open(infile, "r", encoding='utf-8') as fin, open(outfile, "w", encoding='utf-8') as fout:
        # Đọc dữ liệu từ file input
        lines = fin.read().strip().split('\n')
        t = int(lines[0])
        data = [t]
        
        for i in range(1, t + 1):
            data.append(lines[i])
        
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