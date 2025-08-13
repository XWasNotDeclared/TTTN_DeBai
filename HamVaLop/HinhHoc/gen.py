import os

def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách string đã được đọc từ input.
    - TODO: Viết logic giải ở đây.
    - Trả về: list (hoặc iterable) chứa các dòng kết quả (string hoặc số).
    """
    PI = 3.14159
    lines = data.strip().split('\n')
    n = int(lines[0])
    result = []
    
    for i in range(1, n + 1):
        line = lines[i].split()
        shape_type = line[0]
        
        if shape_type == "RECT":
            w = int(line[1])
            h = int(line[2])
            area = w * h
            perimeter = 2 * (w + h)
        elif shape_type == "CIRCLE":
            r = int(line[1])
            area = PI * r * r
            perimeter = 2 * PI * r
        
        result.append(f"{area:.2f} {perimeter:.2f}")
    
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
    Giữ nguyên phần này cho các bài sau, trừ khi định dạng input/output thay đổi.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu từ file input
        data = fin.read().strip()
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